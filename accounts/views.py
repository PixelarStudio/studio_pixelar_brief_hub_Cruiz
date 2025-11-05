from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm

def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect("home")
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/signup.html", {"form": form})

@login_required
def profile(request):
    return render(request, "accounts/profile.html")

@login_required
def edit_profile(request):
    if request.method == "POST":
        u_form = UserEditForm(request.POST, instance=request.user)
        p_form = ProfileEditForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect("profile")
    else:
        u_form = UserEditForm(instance=request.user)
        p_form = ProfileEditForm(instance=request.user.profile)
    return render(
        request,
        "accounts/profile_edit.html",
        {"u_form": u_form, "p_form": p_form},
    )

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Contraseña actualizada.")
            return redirect("profile")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "accounts/change_password.html", {"form": form})
