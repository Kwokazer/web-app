from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from amonic_app.forms import CustomAuthenticationForm
class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('login') 