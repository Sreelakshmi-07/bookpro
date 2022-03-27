from django.shortcuts import render, redirect
from book_form.models import Books
from django.views.generic import View
from customer.forms import UserRegistrationForm, LoginForm,PasswordRestForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


# Create your views here.
class CustomerIndex(View):

    def get(self, request):
        qs = Books.objects.all()
        return render(request, 'home_customer.html', {'books': qs})


class SignupView(View):
    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm()
        return render(request, "signup.html", {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customerhome')
        else:
            return render(request, 'signup.html', {'form': form})


class SigninView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'signin.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                print("login success")
                login(request, user)
                return redirect('customerhome')
            else:
                print("login failed")
                return render(request, "signin", {'form': form})

def signout(request):
    logout(request)
    return redirect('signin')

# class PasswordRestView(View):
#     def get(self,request,*args):
#         form = PasswordResetForm()
#         return render(request,'password_reset.html',{'form':form})
#     def post(self,request):
#         form = PasswordResetForm(request.POST)
#         if form.is_valid():
#             old_password = form.cleaned_data.get('old_password')
#             new_password = form.cleaned_data.get('new_password')
#             messages.info(request, 'Your password has been changed successfully!')
#             user = authenticate(request,username = request.user,password = old_password)
#             if user:
#                 user.set_password(new_password)
#                 user.save()
#                 return redirect('customerhome')
#             else:
#                 return render(request, 'password_reset.html', {'form': form})
#         else:
#             return render(request, 'password_reset.html', {'form': form})
class PasswordRestView(View):
    def get(self,request):
        form = PasswordRestForm()
        return render(request,'password_reset.html',{'form':form})
    def post(self,request):
        form = PasswordRestForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data.get('old_password')
            new_password = form.cleaned_data.get('new_password')
            user = authenticate(request,username = request.user,password = old_password)
            if user:
                user.set_password(new_password)
                user.save()
                return redirect('signin')
            else:
                return render(request, 'password_reset.html', {'form': form})
        else:
            return render(request, 'password_reset.html', {'form': form})

