# home/adapters.py
from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from allauth.account.views import SignupView
from allauth.account import signals
from django.contrib.auth import logout
from allauth.account.models import Login
from allauth.account.internal import flows
from allauth.account.forms import SignupForm, LoginForm

class CustomLoginForm(LoginForm):
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('login')
        password = cleaned_data.get('password')

        # Verifica se o username e password foram fornecidos
        if username and password:
            from django.contrib.auth import authenticate
            user = authenticate(username=username, password=password)

            if user is None or not user.is_staff:
                raise ValidationError("Apenas usuários com permissão de staff podem fazer login.")
        
        return cleaned_data
    
class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        # Envie o sinal de usuário registrado
        signals.user_signed_up.send(sender=self.__class__, request=request, user=user)
        return user

class CustomSignupView(SignupView):
    form_class = CustomSignupForm

    def form_valid(self, form):
        # Chama o método save do formulário personalizado
        self.user = form.save(self.request)
        
        # Adiciona uma mensagem de sucesso
        messages.success(self.request, 'Cadastro realizado com sucesso! Por favor, entre em contato com um administrador para liberar o acesso.')
        
        # Redireciona para a página de login
        return redirect(reverse('account_login'))