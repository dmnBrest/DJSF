import django
import requests
import sys
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.utils.translation import get_language
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

try:
    from django.utils.encoding import smart_unicode
except ImportError:
    from django.utils.encoding import smart_text as smart_unicode

from constants import TEST_PUBLIC_KEY, TEST_PRIVATE_KEY

class MyReCaptchaField(forms.CharField):

    default_error_messages = {
        'captcha_invalid': _('Captcha is incorrect, please try again.'),
        'captcha_error': _('Error verifying input, please try again.'),
    }

    def __init__(self, *args, **kwargs):

        self.widget = MyReCaptchaWidget()

        self.required = True

        super(MyReCaptchaField, self).__init__(*args, **kwargs)

    def clean(self, values):

        #super(MyReCaptchaField, self).clean(values[0])

        recaptcha_response_value = smart_unicode(values[0])
        if not recaptcha_response_value:
            raise ValidationError(self.error_messages['captcha_invalid'])

        is_valid = self.recaptcha_verify(recaptcha_response_value)

        if not is_valid:
            raise ValidationError(self.error_messages['captcha_invalid'])
        return values[0]


    def get_remote_ip(self):
        f = sys._getframe()
        while f:
            if 'request' in f.f_locals:
                request = f.f_locals['request']
                if request:
                    remote_ip = request.META.get('REMOTE_ADDR', '')
                    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
                    ip = remote_ip if not forwarded_ip else forwarded_ip
                    return ip
            f = f.f_back

    def recaptcha_verify(self, val):
        url = "https://www.google.com/recaptcha/api/siteverify"
        params = {
            'secret': settings.RECAPTCHA_PRIVATE_KEY,
            'response': val,
            'remoteip': self.get_remote_ip()
        }
        print(params)
        verify_rs = requests.get(url, params=params, verify=True)
        verify_rs = verify_rs.json()
        is_valid = verify_rs.get("success", False)
        if not is_valid:
            logger.warning(verify_rs.get('error-codes', None) or 'RECAPTCHA Unspecified error')
        return verify_rs.get("success", False)

class MyReCaptchaWidget(forms.widgets.Widget):
    recaptcha_response_name = 'g-recaptcha-response'
    template_name = 'my_recaptcha/widget.html'

    def __init__(self, *args, **kwargs):
        super(MyReCaptchaWidget, self).__init__(*args, **kwargs)

    def value_from_datadict(self, data, files, name):
        return [
            data.get(self.recaptcha_response_name, None)
        ]

    def render(self, name, value, attrs=None, renderer=None):
        if django.VERSION < (1, 11):
            return mark_safe(render_to_string(
                self.template_name,
                self.get_context(name, value, attrs)
            ))
        else:
            return super(MyReCaptchaWidget, self).render(
                name, value, attrs=attrs, renderer=renderer
            )

    def get_context(self, name, value, attrs):

        try:
            lang = attrs['lang']
        except KeyError:
            # Get the generic language code
            lang = get_language().split('-')[0]

        try:
            context = super(MyReCaptchaWidget, self).get_context(name, value, attrs)
        except AttributeError:
            context = {
                "widget": {
                    "attrs": self.build_attrs(attrs)
                }
            }
        context.update({
            'public_key': settings.RECAPTCHA_PUBLIC_KEY,
            'lang': lang
        })
        return context