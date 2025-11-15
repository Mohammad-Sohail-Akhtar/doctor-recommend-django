from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are able login now')
            return redirect('login')
    else:    
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form': form})





class UserLoginView(LoginView):
    template_name = "users/login.html"

    def form_valid(self, form):
        user = form.get_user()
        if user.is_superuser:
            messages.error(self.request, "Superadmins must log in from /admin/ not here.")
            return redirect("login")  # back to login page
        return super().form_valid(form)


