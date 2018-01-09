import logging
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.conf import settings

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@login_required
def index(request):

    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        print(myfile)
        print(type(myfile))
        print(myfile.content_type)
        print(myfile.size)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return JsonResponse({'message': 'Success'})


    return render(request, 'file_manager/manager.html', {

    })

