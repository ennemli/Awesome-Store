from django.urls import reverse_lazy
from django.views import generic
from .forms import AuthForm,RegisterForm
from .models import ShopByDepartment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views,user_logged_in,user_logged_out
from django.contrib.auth.forms import get_user_model
from django.dispatch import receiver
# Create your views here.
@receiver(user_logged_in)
def loggedinuser(sender=get_user_model(),**kwargs):
    print(kwargs.get('user').username,'just logged in')
@receiver(user_logged_out)
def loggedoutuser(sender=get_user_model(),**kwargs):
    print(kwargs.get('user').username,'just logged out')
class Index(generic.TemplateView):
    template_name = 'index.html'

class Register(generic.FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('awesome_store:login')

class UserLogin(views.LoginView):
    template_name = 'login.html'
    authentication_form = AuthForm

class Profile(LoginRequiredMixin,generic.TemplateView):
    login_url = reverse_lazy('awesome_store:login')
    redirect_field_name = ''
    template_name = 'profile.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['user']=self.request.user
        return context

class UserLogout(views.LogoutView):
    next_page = reverse_lazy('awesome_store:index')
