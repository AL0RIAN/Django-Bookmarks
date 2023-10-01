from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request: HttpRequest) -> HttpResponse:
    context = {
        'section': 'dashboard'
    }
    return render(request, 'account/dashboard.html', context=context)


def user_login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    context = {
        "form": form,
    }

    return render(request, 'account/login.html', context=context)
