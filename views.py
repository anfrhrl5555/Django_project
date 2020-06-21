from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from .models import User, cleanText, re
# Create your views here.
def register(request):
    
    if request.method == "GET":
        return render(request, 'register.html')

    elif request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re_password', None)
        res_data = {}

        if username == cleanText(username):
            try:
                user = User.objects.get(username=username)
                res_data['error'] = "이미 존재하는 id입니다."
            except:
                if not (username and password and re_password) :
                    res_data['error'] = "모든 값을 입력해야 합니다."
                else:
                    if password != re_password :
                        res_data['error'] = '비밀번호가 다릅니다.'
                    else:
                        if (username and password and re_password ):
                            user = User(username=username, password=make_password(password))
                            user.save()
                            return redirect('/')
                return render(request, 'register.html', res_data)
            return render(request, 'register.html', res_data)
        else:
            res_data['error'] = "특수문자는 사용할 수 없습니다."
            return render(request, 'register.html', res_data)

def login(request) :
    response_data = {}

    try:
        if request.method == "GET":
            return render(request, 'login.html')

        elif request.method == "POST":
            login_username = request.POST.get('username', None)
            login_password = request.POST.get('password', None)

            if not (login_username and login_password):
                    response_data['error'] = "아이디와 비밀번호를 모두 입력해주세요."

            else:
                if login_username == cleanText(login_username):
                    try:
                        user = User.objects.get(username=login_username)
                        if  check_password(login_password, user.password):
                            request.session['user'] = user.id
                            return redirect('appmy/success')
                        else:
                            response_data['error'] = "틀립니다."
                    except: 
                        response_data['error'] = "틀립니다."
                        return render(request, 'login.html', response_data)
                else:
                    response_data['error'] = "id에 특수문자는 사용할수 없습니다."
                    return render(request, 'login.html', response_data)

            return render(request, 'login.html', response_data)
    except:
         return render(request, 'login.html', response_data)
def logout(request):
    request.session.pop('user')
    return redirect('/')

def success(request):
    return render(request, 'success.html')