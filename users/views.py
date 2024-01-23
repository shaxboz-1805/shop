from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from shop.models import CartItem
from users.forms import SignUpForm, SignInForm, EditProfileForm,ChangePasswordForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)    
            return redirect('sign_in')
    form = SignUpForm()
    return render(request, 'sign_up.html', {'form' : form})


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)    
            return redirect('product_list')
    form = SignInForm()
    return render(request, 'sign_in.html', {'form' : form})


def sign_out(request):
    print(request.user)
    logout(request)
    return redirect('sign_in')


def create_order(request):
    cart_items = CartItem.objects.filter(customer=request.user)


def edit_profile(request):
    form = EditProfileForm(request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form' : form})


def reset_password(request):
    form = ChangePasswordForm(request.user, request.POST)
    print(request.method == 'POST')
    print(form.errors, '-----------------')
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        return redirect('sign_in')
    form =ChangePasswordForm(request.user)
    return render(request, 'reset_password.html', {'form' : form})