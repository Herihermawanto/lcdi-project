
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from appLcdi .views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(), name='keluar'),
]
