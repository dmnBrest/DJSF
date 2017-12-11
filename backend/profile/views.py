import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from pprint import pprint
from django.contrib.auth.models import User
from django.core import serializers
from rest_framework.renderers import JSONRenderer

from djsf.serializers import UserSerializer

@login_required
def index(request):

    # send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     'from@example.com',
    #     ['to@example.com'],
    #     fail_silently=False,
    # )
    #
    # print('Send mail')

    pprint(request.user)
    pprint(request.user.is_superuser)
    pprint(request.user.id)
    u = User.objects.get(id=request.user.id)
    print(u)
    pprint(u)
    print(serializers.serialize('json', [u]))
    print('XXXXX')
    print(UserSerializer(u, context={'request': request}).data)
    print(JSONRenderer().render(UserSerializer(u, context={'request': request}).data))

    if request.user.is_superuser:
        return redirect('admin:index')


    messages.add_message(request, messages.SUCCESS, 'Welcome to profile page!!!')
    # messages.add_message(request, messages.INFO, 'Hello world.')
    # messages.add_message(request, messages.ERROR, 'Hello world.')
    # messages.add_message(request, messages.WARNING, 'Hello world.')




    return render(request, 'profile/index.html', {})