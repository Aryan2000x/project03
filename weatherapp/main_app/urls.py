from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('accounts/signup/', views.signup, name='signup'),
    # refer to https://medium.com/@frfahim/django-registration-with-confirmation-email-bb5da011e4ef
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]