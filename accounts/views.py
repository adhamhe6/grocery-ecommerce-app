from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomPasswordChangeForm, CustomSetPasswordForm, CustomPasswordResetForm
from django.urls import reverse_lazy
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'This email address is already in use.')
            else:
                user = form.save()
                user_profile, created = UserProfile.objects.get_or_create(user=user)
                if created:
                    user_profile.save()
                return redirect(reverse_lazy('accounts:sign_in'))
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

@ensure_csrf_cookie
@csrf_protect
def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('pages:index'))
        else:
            #messages.info(request, 'username or password is incorrect')
            pass
    context = {}
    return render(request, 'accounts/login.html', context)

@login_required
def sign_out(request):
    logout(request)
    #messages.success(request,f'You have been logged out.')
    return redirect('accounts:sign_in') 

def password_reset_view(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('accounts:password_reset_done'))
    else:
        form = CustomPasswordResetForm()
    
    return render(request, 'accounts/password_reset.html', {'form': form})

def password_reset_done_view(request):
    return render(request, 'accounts/password_reset_done.html')

def password_reset_confirm_view(request, uidb64, token):
    if request.method == 'POST':
        form = CustomSetPasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('accounts:password_reset_complete'))
    else:
        form = CustomSetPasswordForm(request.user)
    
    return render(request, 'accounts/password_reset_confirm.html', {'form': form})

def password_reset_complete_view(request):
    return render(request, 'accounts/password_reset_complete.html')

@ensure_csrf_cookie
@csrf_protect
@login_required
def password_change_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('accounts:password_change_done'))
    else:
        form = CustomPasswordChangeForm(request.user)
    
    return render(request, 'accounts/password_change.html', {'form': form})

def password_change_done_view(request):
    return render(request, 'accounts/password_change_done.html')




# @login_required
# def profile(request):
#     user_profile = request.user.profile
#     return render(request, 'accounts/profile.html', {'user_profile': user_profile})
