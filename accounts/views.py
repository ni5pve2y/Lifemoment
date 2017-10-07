from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from accounts.forms import RegistrationForm, EditProfileForm, ChangeImageForm
from accounts.models import UserProfile, Friend
from posts.models import Post


def profile(request, current_user):
    user = get_object_or_404(User, username=current_user)

    context = {
        'user': user,
        'user_profile': UserProfile.objects.get(user=user),
        'posts': Post.objects.filter(user=user),
    }
    return render(request, 'accounts/profile.html', context)


def information(request, current_user):
    user = get_object_or_404(User, username=current_user)

    context = {
        'user': user,
        'user_profile': UserProfile.objects.get(user=user),
    }
    return render(request, 'accounts/information.html', context)


def friends(request, current_user):
    user = get_object_or_404(User, username=current_user)
    user_friends, created = Friend.objects.get_or_create(current_user=user)

    context = {
        'user': user,
        'friends': user_friends.users.all(),
        'user_profile': UserProfile.objects.get(user=user),
    }
    return render(request, 'accounts/friends.html', context)


def add_friend(request, current_user, new_friend):
    user = get_object_or_404(User, username=current_user)
    friend = get_object_or_404(User, username=new_friend)
    Friend.add_friend(current_user=user, new_friend=friend)
    return redirect('accounts:friends', current_user=request.user)


def settings(request, current_user):
    user = get_object_or_404(User, username=current_user)
    if user == request.user:
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile details updated.')
                return redirect('accounts:settings', current_user=request.user)
            else:
                messages.error(request, 'Profile details not updated.')
                return redirect('accounts:settings', current_user=request.user)
        else:
            form = EditProfileForm(instance=request.user)
            context = {
                'form': form,
            }
            return render(request, 'accounts/settings.html', context)
    else:
        raise Http404


def change_password(request, current_user):
    user = get_object_or_404(User, username=current_user)
    if user == request.user:
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Password has been changed.')
                return redirect('accounts:settings', current_user=request.user)
            else:
                messages.error(request, 'Password has not been changed')
                return redirect('accounts:change_password', current_user=request.user)
        else:
            form = PasswordChangeForm(user=request.user)
            context = {
                'form': form,
            }
            return render(request, 'accounts/change_password.html', context)


def change_image(request, current_user):
    user = get_object_or_404(User, username=current_user)
    user_profile = get_object_or_404(UserProfile, user=user)
    if user == request.user:
        if request.method == 'POST':
            form = ChangeImageForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                messages.success(request, 'Image has been changed.')
                return redirect('accounts:settings', current_user=request.user)
            else:
                messages.error(request, 'Image has not been changed')
                return redirect('accounts:change_image', current_user=request.user)
        else:
            form = ChangeImageForm(instance=user_profile)
            context = {
                'form': form,
            }
            return render(request, 'accounts/change_password.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('accounts:login')
    else:
        context = {
            'form': RegistrationForm(),
        }
        return render(request, 'accounts/register.html', context)


def startpage(request):
    return render(request, 'accounts/startpage.html', {})
