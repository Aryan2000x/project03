import requests
from django.http import HttpResponse
from django.shortcuts import render
#imports for login
from django.contrib.auth import login, authenticate
# imports for signup forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#for more information about these imports, please checkout this blog: https://medium.com/@frfahim/django-registration-with-confirmation-email-bb5da011e4ef
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
# get token for email and passwordreset confirmations
from .tokens import account_activation_token
# email
from django.core.mail import EmailMessage

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

# Define the home view

def index(request):
  url= "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=615565f33a31c50af502c7ff0810f560"

  city = 'Toronto'

  r = requests.get(url.format(city)).json()

  city_weather = {
    'city': city ,
    'temperature': r['main']['temp'],
    'description' : r ['weather'][0]['description'],
    'icon': r['weather'][0]['icon'],
  }
  
  context = {'city_weather': city_weather}

  return render(request, 'weather/weather.html', context)
    
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your Weather account.'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
