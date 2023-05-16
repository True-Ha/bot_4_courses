from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView

from .forms import LoginForm
from app.models import MyUser, Training


class HomePage(ListView):
    model = Training
    template_name = 'weeks/train_list.html'
    context_object_name = 'train_home_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['train_list'] = Training.objects.all().order_by('id')
        return context



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


def get_train():
    return Training.objects.all()


class TrainingView(ListView):
    model = Training
    template_name = 'weeks/train_list.html'
    context_object_name = 'trainings'

    def get_queryset(self):
        return Training.objects.all()



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['train_list'] = Training.objects.all().order_by('id')
        context['1st_week'] = Training.objects.filter(name__contains='1st').order_by('id')
        context['2nd_week'] = Training.objects.filter(name__contains='2nd').order_by('id')
        context['3rd_week'] = Training.objects.filter(name__contains='3rd').order_by('id')
        context['4th_week'] = Training.objects.filter(name__contains='4th').order_by('id')

        return context


class TrainingsDaysView(DetailView):
    model = Training
    template_name = 'weeks/train_detail.html'
    context_object_name = "train"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['1st_week'] = Training.objects.filter(name__contains='1st').order_by('id')
        context['header_week'] = Training.objects.filter(name__contains='mon').order_by('id')
        context['3rd_week'] = Training.objects.filter(name__contains='3rd').order_by('id')
        context['4th_week'] = Training.objects.filter(name__contains='4th').order_by('id')
        return context