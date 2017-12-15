import logging
import io
import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from profile.models import UserProfile
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from django.forms.models import model_to_dict

from djsf.serializers import UserSerializer;
from profile.serializers import  UserProfileSerializator

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@login_required
def index(request):

    if request.user.is_superuser:
        return redirect('admin:index')

    # send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     'from@example.com',
    #     ['to@example.com'],
    #     fail_silently=False,
    # )
    #
    # print('Send mail')

    # pprint(request.user)
    # pprint(request.user.is_superuser)
    # pprint(request.user.id)

    logger.debug('XXXXX')

    u = User.objects.get(id=request.user.id)
    u1 = model_to_dict(u, fields=['id', 'email', 'username', 'last_login'])
    uu1 = JSONRenderer().render(u1)
    logger.debug(uu1)
    uu2 = JSONParser().parse(io.BytesIO(uu1))
    u2 = User(**uu2)
    logger.debug(u2)
    logger.debug(u2.last_login)


    # u1 = UserSerializer(u).data
    # # uu1 = JSONRenderer().render(u1)
    # # uu2 = JSONParser().parse(io.BytesIO(uu1))
    #
    # logger.debug(u1)
    # u1['is_staff'] = True
    # logger.debug(u1)
    #
    # u2 = UserSerializer(u, data=u1)
    # logger.debug(u2.is_valid())  # => False
    # logger.debug(u2.validated_data['is_staff'])
    # logger.debug(u2.data)
    # logger.debug(u2.errors)  # => {'username': ['A user with that username already exists.']}



    # resp = {}
    #
    # u = User.objects.get(id=request.user.id)
    # u_ = UserSerializer(u).data
    #
    # resp['user'] = u_
    #
    # logger.debug(u_)
    # logger.debug(type(u_))
    #
    # up = UserProfile.objects.get(user_id=2)
    # up_ = UserProfileSerializator(up).data
    #
    # resp['profile'] = up_
    #
    # logger.debug(up_)
    # logger.debug(type(up_))
    #
    # respJSON = JSONRenderer().render(resp)
    #
    # logger.debug(respJSON)
    # logger.debug(type(respJSON))
    #
    # data2 = JSONParser().parse(io.BytesIO(respJSON))
    #
    # u2_ = UserSerializer(data=data2['user'])
    #
    # # up2_ = UserProfileSerializator(data=data2['profile'])
    #
    #
    # logger.debug(u2_)
    # logger.debug(u2_.is_valid())
    # logger.debug(u2_.errors)
    # logger.debug(u2_.data)
    # logger.debug(u2_.instance)
    # #logger.debug(u2_.instance.username)
    # logger.debug(type(u2_))

    # logger.debug(up2_)
    # logger.debug(up2_.is_valid())
    # logger.debug(up2_.errors)
    # logger.debug(up2_.data)
    # logger.debug(type(up2_))

    #logger.debug(JSONRenderer().render(UserProfileSerializator(up).data))

    messages.add_message(request, messages.SUCCESS, 'Welcome to profile page!!!')
    # messages.add_message(request, messages.INFO, 'Hello world.')
    # messages.add_message(request, messages.ERROR, 'Hello world.')
    # messages.add_message(request, messages.WARNING, 'Hello world.')




    return render(request, 'profile/index.html', {})