from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from .forms import LoginForm


class LoginView(View):

    def get(self, request, *args, **kwargs):
        context = {'form': LoginForm}
        return render(request, 'login.html', context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('user-info')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')


class UserView(View):

    def get(self, request, *args, **kwargs):
        context = {
            'user': request.user
        }
        return render(request, 'profile_detail.html', context)

