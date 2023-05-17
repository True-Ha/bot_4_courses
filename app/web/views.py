from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, UpdateView

from .forms import LoginForm, UserUpdateForm
from app.models import MyUser, Training


class HomePage(ListView):
    model = Training
    template_name = 'weeks/train_list.html'
    context_object_name = 'train_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['train_list'] = Training.objects.all().order_by('id')
        return context


class UserView(DetailView):
    model = MyUser
    template_name = 'accounts/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def update_user(request):
    if request.user.is_authenticated:
        current_user = MyUser.objects.get(id=request.user.id)
        form = UserUpdateForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            login(request, current_user)
            messages.success(request, ("Profile updated"))
            return redirect('home')
        return render(request, 'accounts/user-upgrade.html', {'form': form})
    else:
        messages.success(request, ("You must be logged"))
        return redirect('home')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_train():
    return Training.objects.all()


class TrainingsDaysView(DetailView):
    model = Training
    template_name = 'weeks/train_detail.html'
    context_object_name = "train"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        days_week = self.kwargs['slug']
        days_week = days_week[0]
        context['header_week'] = Training.objects.filter(name__contains='mon').order_by('id')
        context['day_list'] = Training.objects.filter(name__contains=days_week)
        return context


