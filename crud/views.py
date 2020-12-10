from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.contrib import messages
from rest_framework import permissions
from rest_framework import permissions
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User

from .forms import StudentRegistration
from .models import Crud_Users
from .models import InfogeonUsers

# from models import InfogeonUsers

# from .serializers import UserSerializer

# @login_required(login_url="login")
# def home(request):add_show
#
#     context = {}
#     return render(request,'enroll/addandshow.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('addandshow')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('addandshow')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'users/login.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'User logged out.')
    return redirect('login')


# @login_required(login_url="login")
def userPage(request):
    user_address = request.user.address.all()
    user_roles = request.user.roles.all()

    context = {'saved_address': user_address, 'user_roles': user_roles}

    return render(request, 'users/user.html', context)


# Create your views here.
def add_show(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = StudentRegistration(request.POST)
            if fm.is_valid():
                nm = fm.cleaned_data['name']
                em = fm.cleaned_data['email']
                pw = fm.cleaned_data['password']
                reg = Crud_Users(name=nm, email=em, password=pw)
                reg.save()
            fm = StudentRegistration()
        else:
            fm = StudentRegistration()
            # stud = Crud_Users.objects.all()
            stud = InfogeonUsers.objects.all()
            # stud = InfogeonUsers.objects.all().values()
            # stud = InfogeonUsers._meta
        return render(request, 'enroll/addandshow.html', {'form': fm,
                                                          'stu': stud})
    else:
        return redirect('login')

# class UserViewSet(APIView):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Crud_Users.objects.all().order_by('-id')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


