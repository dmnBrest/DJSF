from widgets.my_recaptcha import MyReCaptchaField
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    captcha = MyReCaptchaField()