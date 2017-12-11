from django.conf import settings

def global_settings(request):
    # return any necessary values
    return {
        'SLDS_URL': settings.SLDS_URL
    }