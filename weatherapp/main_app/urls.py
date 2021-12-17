from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.Weather.index, name='index'),
    path('delete/<city_name>/', views.delete_city, name='delete_city'),
    path('accounts/signup/', views.signup, name='signup'),
    # refer to https://medium.com/@frfahim/django-registration-with-confirmation-email-bb5da011e4ef
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]