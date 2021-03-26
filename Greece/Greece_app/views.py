from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

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

class Contactpage(TemplateView):
    template_name= "contactus.html"
    def post(self, request):

        form = request.POST
        name = form.get('name')
        email = form.get('email')
        phone = form.get('phone')
        subject = form.get('subject')
        message = form.get('message')

        new_contact = models.Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message

        )
        new_contact.save()
        mailHandler.sendMailToUser(name, email)
        mailHandler.sendMailToVisaToCanada(name, email, phone, subject, message)
        messages.success(request, "Your query has been successfully submitted. We will get back to you soon.")
        return redirect("contactus")


