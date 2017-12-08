from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html', {})

def ng_test(request):
    return render(request, 'home/ng_test.html', {})