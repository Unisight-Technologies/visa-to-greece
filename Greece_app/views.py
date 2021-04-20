from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from . import mailHandler
from . import models
#recaptcha imports
import json
import urllib
from django.conf import settings
import environ
env = environ.Env()
# reading .env file
environ.Env.read_env()

# Create your views here.
class Homepage(TemplateView):
    template_name= "index.html"

class Terms(TemplateView):
    template_name= "terms.html"

class Disclaimer(TemplateView):
    template_name= "disclaimer.html"

class Privacypolicy(TemplateView):
    template_name= "privacy_policy.html"

class Comingpage(TemplateView):
    template_name= "coming_soon.html"

class Studentvisapage(TemplateView):
    template_name= "studentvisa.html"

class Aboutuspage(TemplateView):
    template_name= "aboutus.html"

class Workvisapage(TemplateView):
    template_name= "workvisa.html"

class Goldenvisapage(TemplateView):
    template_name= "golden_visa.html"

class Givingitback(TemplateView):
    template_name= "givingItBack.html"

class Contactpage(View):
    def get(self, request, *args, **kwargs):
        context={
            'SITE_KEY': env('RECAPTCHA_SITE_KEY')
        }

        return render(request, "contactus.html",context = context)
    
    def post(self, request, *args, **kwargs):
        data = request.POST
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''
        if result['success']:
            mailHandler.sendMailToUser(request.POST.get('name'), request.POST.get('email'))
            mailHandler.sendMailToVisaToGreece(request.POST.get('name'), request.POST.get('email'),request.POST.get('phone'),request.POST.get('subject'),request.POST.get('message'))
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')
        else:
            messages.info(request, 'Invalid reCAPTCHA. Please try again.')
            context={
            'SITE_KEY': env('RECAPTCHA_SITE_KEY')
            }
            return render(request,"contactus.html",context = context)

class News(View):
    def get(self, request, *args, **kwargs):
        news=models.News.objects.all()
        context={
        "all_news":news,
        "info":"mydata",
        }
        print(news)

        return render(request, "news.html",context=context)
