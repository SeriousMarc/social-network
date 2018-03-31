from django.shortcuts import render, redirect

def homepage(request):
    request.session.set_test_cookie()
    return render(request, '../templates/base_layout.html')
