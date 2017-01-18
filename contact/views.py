import json
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template import Context
from django.template.loader import get_template
from contact.forms import ContactForm
from contact.models import ContactModel


__author__ = 'user'

def contact_view(request):

   if request.method == 'POST':
       print(request.POST)
       form = ContactForm(data=request.POST)
       if form.is_valid():
           contact_name = request.POST.get(
               'contact_name'
               , '')
           contact_email = request.POST.get(
               'contact_email'
               , '')
           message = request.POST.get('message', '')
           # Email the profile with the
           # contact information
           stemplate = get_template('contact_template.txt')
           context = Context({'contact_name': contact_name, 'contact_email': contact_email, 'message': message,})
           content = stemplate.render(context)
           email = EmailMessage("New contact form submission", content, "DreamINTechs" + '', ['merlin.sayone@gmail.com'], headers={'Reply-To': contact_email})
           email.to = ["merlin.sayone@gmail.com"]
           email.send()


           print("****************************",email)
           profile_obj = ContactModel.objects.create(
               contact_name = contact_name,
               contact_email = contact_email,
               message = message,
               )
           profile_obj.save()
           resp={'status': 'success'}
           return HttpResponse(json.dumps(resp))
       else:
           resp={'status': 'failed', 'data': form.errors}
           return HttpResponse(json.dumps(resp))

   else:
       form = ContactForm()

   return render(request, 'contact.html', {'form': form, })





