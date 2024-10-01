from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site URL
    path('', auth_views.LoginView.as_view(), name='login'),  # Redirect root URL to built-in login view
]
