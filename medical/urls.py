"""
URL configuration for medical project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as user_views
from machine import views as new_views
from machine import views as app_views
from machine import views as con_views
from machine import views as del_views
from machine import views as edit_views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name ='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name ='users/logout.html'), name='logout'),
    path('', include('main_app.urls')),
    path("book/", new_views.book_appointment, name="book"),
    path("appointments/", app_views.my_appointments, name="appointments"),
    path("confirm/", con_views.confirm_appointment, name="confirm_appointment"),
    path('appointments/delete/<int:appointment_id>/', del_views.delete_appointment, name='delete_appointment'),
    path('appointments/edit/<int:appointment_id>/', edit_views.edit_appointment, name='edit_appointment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
