from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from . import mailHandler
from . import models

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
        return render(request,"contactus.html")
    
    def post(self, request, *args, **kwargs):
        data=request.POST
        mailHandler.sendMailToUser(data.get('name'), data.get('email'))
        mailHandler.sendMailToVisaToGreece(data.get('name'), data.get('email'), data.get('phone'), data.get('subject'),data.get('message'))
        print(request.POST)
        return redirect("index")

class News(View):
    def get(self, request, *args, **kwargs):
        news=models.News.objects.all()
        context={
        "all_news":news,
        "info":"mydata",
        }
        print(news)

        return render(request, "news.html",context=context)
