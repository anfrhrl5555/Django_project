from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User
# Create your views here.

def home(request):
    # return render(request, 'home.html')
    user_id = request.session.get('user')
    if user_id:
        user_info = User.objects.get(pk=user_id)
        return HttpResponse(user_info.username)
    # return render(request, 'login.html')
    return HttpResponse('우아아앙')

def register(request):
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        res_data = {}
        if not (username or password or re_password) :
            res_data['error'] = "모든 값을 입력해야 합니다."

        if password != re_password :
            res_data['error'] = '비밀번호가 다릅니다.'

        if (username and password and re_password ):
            user = User(username=username, password=make_password(password))
            user.save()
            return render(request, 'login.html')

        else:
            return render(request, 'register.html', res_data)


def login(request) :
    response_data = {}

    if request.method == "GET":
        return render(request, 'login.html')

    elif request.method == "POST":
        login_username = request.POST.get('username', None)
        login_password = request.POST.get('password', None)

        if not (login_username and login_password):
                response_data['error'] = "아이디와 비밀번호를 모두 입력해주세요."
asas
        else:
            user = User.objects.get(username=login_username)

            if check_password(login_password, user.password):
                request.session['user'] = user.id
                return redirect('appmy/success')

            if not check_password(login_password, user.password):
                # return redirect('appmy/success')
                # response_data['error'] = "아이디와 비밀번호를 모두 입력해주세요"
                return render(request, 'login.html')

        return render(request, 'login.html', response_data)

def logout(request):
    request.session.pop('user')
    return redirect('/')
#
def success(request):
    return render(request, 'success.html')