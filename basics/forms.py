from django import forms
from django.contrib.auth.models import User
from .models import Need, Information, Userdata
from nocaptcha_recaptcha.fields import NoReCaptchaField


class UserFormRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password','email']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

class NeedFormNew(forms.ModelForm):
	class Meta:
		model = Need
		fields = ['headline','text']

class InformationFormNew(forms.ModelForm):
	class Meta:
		model = Information
		fields = ['headline','text']

class CaptchaForm(forms.Form):
    captcha = NoReCaptchaField()

class ProfileForm(forms.Form):
	class Meta:
		model = Userdata
		fields= ['pseudonym','phone',]
