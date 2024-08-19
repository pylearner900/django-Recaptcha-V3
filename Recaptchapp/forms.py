from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

class MyForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    captcha = ReCaptchaField(
        widget=ReCaptchaV3
        (
            attrs={
            'required_score':0.85,
        }),
        
    )
