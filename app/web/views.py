from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView

from .forms import LoginForm
from app.models import MyUser


# class HomePage(View):
#     def get(self, request):
#         return render(request, 'home.html')

class HomePage(TemplateView):
    template_name = 'home.html'



class LoginView(View):

    def get(self, request, *args, **kwargs):
        context = {'form': LoginForm}
        return render(request, 'accounts/login.html', context)

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


class UserView(DetailView):
    model = MyUser
    template_name = 'accounts/profile_detail.html'


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


######Training#####
class FstWeek(TemplateView):
    template_name = 'weeks/1st_week.html'


class ScndWeek(TemplateView):
    template_name = 'weeks/2nd_week.html'


class ThrdWeek(TemplateView):
    template_name = 'weeks/3rd_week.html'


class FourthWeek(TemplateView):
    template_name = 'weeks/4th_week.html'

# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['--'] = Post.objects.filter(draft=False).order_by('-date')
#     context['Mon'] =
#     context['Wed'] =
#     context['Fri'] =
#     return context
