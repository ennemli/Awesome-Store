from django import forms
from .models import User
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm


def commonClassName( fields, className):
    for field in fields.keys():

        fields[field].widget.attrs.update({'class': className})

class AuthForm(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        commonClassName(self.fields,'form-control')
    def confirm_login_allowed(self, user):
        pass

class XBackend(ModelBackend):
    def authenticate(self, email=None,password=None,**kwargs):
        pass

class RegisterForm(UserCreationForm):
    birthday=forms.CharField(widget=forms.DateTimeInput)
    class Meta:
        model = User
        exclude = ('password','is_superuser','groups','user_permissions','last_login')
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        commonClassName(self.fields,'form-control')



