from django.contrib.auth.models import User, auth
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PersonCreationForm
from .models import Person, Branch


def base(request):
    return render(request, 'base.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if not username:
            return render(request,'register.html')

        if not password:
            return render(request,'register.html')

        if not confirm_password:
            return render(request,'register.html')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.set_password(password)
                user.is_staff = False
                user.save()
                return redirect('login_user')
    else:
        print("this is not post method")
        return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        # if not username:
        #     messages.info(request, 'enter username')
        #     return render(request,'login_user')

        # if not password:
        #     messages.info(request, 'enter password')
        #     return render(request,'login_user')



        if user is not None:
            auth.login(request, user)
            return redirect('new')
        else:
            messages.info(request, 'Invalid username or password')
            print('invalid password or username')
            return redirect('login_user')

    else:
        return render(request, 'login.html')





def person_create_view(request):
    form = PersonCreationForm()

    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accept')
    else:
        form=PersonCreationForm()
    return render(request, 'persons/home.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'persons/home.html', {'form': form})


# AJAX
def load_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'persons/city_dropdown_list_options.html', {'branches': branches})
    # return JsonResponse(list(branches.values('id', 'name')), safe=False)


def new(request):
    return render(request, 'new.html')

def accept(request):
    return render(request, 'accept.html')

def logout_user(request):
    auth.logout(request)
    return redirect('base')