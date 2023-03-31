from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages
# Create your views here.


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'

def user_login(request):

    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                login(request, user)

                return redirect("dashboard")
            

@login_required
def user_logout(request):
    try:
        for key in list(request.session.keys()):
            if key == 'session_key':
                continue
            else:
                del request.session[key]
    except KeyError:
        pass
    messages.success(request, "Logout success")

    return redirect("gigs:index")

@login_required(login_url='login')
def profile_mangement(request):
    user_form = forms.UpdateUserForm(instance=request.user)

    if request.method == 'POST':
        user_form = forms.UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.info(request, "Update success!")
            return redirect('dashboard')
    context = {'user_form':user_form}

    return render(request, 'account/profile-management.html', context=context)