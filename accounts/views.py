from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import SignupForm,LoginForm, ResetPasswordForm
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect



User = get_user_model()


class SignupView(FormView):
    template_name = 'accounts/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()  # password is already hashed in form.save()
        messages.success(self.request, "Account created successfully! You can now log in.")
        return super().form_valid(form)

# LOGIN VIEW....

class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('signup')  # redirect to signup page after login

    def form_valid(self, form):
        user = form.cleaned_data['user']
        login(self.request, user)
        messages.success(self.request, f"Welcome back, {user.email}!")
        return super().form_valid(form)

    
# RESET PASSWORD VIEW

User = get_user_model()

class ResetPasswordView(FormView):
    template_name = 'accounts/reset_password.html'
    form_class = ResetPasswordForm
    success_url = reverse_lazy('login')

    # Remove dispatch() completely
    # We don’t need kwargs or email anymore

    def form_valid(self, form):
        # Pick the first user (or change logic as needed)
        user = User.objects.first()
        user.set_password(form.cleaned_data['new_password'])
        user.save()
        messages.success(self.request, "Password reset successfully! You can now login.")
        return super().form_valid(form)
    
# logout view...

class CustomLogoutView(LogoutView):
    next_page = 'login'  # redirect to login page

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been logged out successfully.")
        return super().dispatch(request, *args, **kwargs)




