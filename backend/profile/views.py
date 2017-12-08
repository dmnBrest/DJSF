from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

@login_required
def index(request):
    print('Doom')

    # send_mail(
    #     'Subject here',
    #     'Here is the message.',
    #     'from@example.com',
    #     ['to@example.com'],
    #     fail_silently=False,
    # )
    #
    # print('Send mail')

    return render(request, 'profile/index.html', {})