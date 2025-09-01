from django.shortcuts import render, redirect
from .models import Service, Testimonial, FAQ
from .forms import LeadForm

DEFAULT_MAP = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d387143.3074413584!2d-74.25987568725828!3d40.69767006759679!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zNDDCsDQxJzUxLjYiTiA3NMKwMTUnMjIuMiJX!5e0!3m2!1sen!2sus!4v1600000000000"
DEFAULT_WHATSAPP = "9198903493735"
Keerthana = "Keerthana"

def home(request):
    services = Service.objects.all()[:6]
    testimonials = Testimonial.objects.all()[:6]
    counters = {'clients': 1200, 'policies': 3500, 'years': 12}
    return render(request, 'core/home.html', {'services': services, 'testimonials': testimonials, 'counters': counters})

def about(request):
    faqs = FAQ.objects.all()
    return render(request, 'core/about.html', {'faqs': faqs})

def services(request):
    services = Service.objects.all()
    return render(request, 'core/services.html', {'services': services})

def contact(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/contact.html', {'form': LeadForm(), 'success': True, 'map_embed_url': DEFAULT_MAP, 'whatsapp_number': DEFAULT_WHATSAPP, 'contact_person': Keerthana})
    else:
        form = LeadForm()
    return render(request, 'core/contact.html', {'form': form, 'map_embed_url': DEFAULT_MAP, 'whatsapp_number': DEFAULT_WHATSAPP, 'contact_person': Keerthana})

def quote(request):
    result = None
    if request.method == 'POST':
        insurance_type = request.POST.get('insurance_type')
        try:
            coverage = float(request.POST.get('coverage', 0))
        except (ValueError, TypeError):
            coverage = 0.0
        rates = {'life':0.005, 'health':0.01, 'vehicle':0.015, 'business':0.02}
        rate = rates.get(insurance_type, 0.01)
        premium = round(coverage * rate, 2)
        result = {'insurance_type': insurance_type, 'coverage': coverage, 'premium': premium}
    return render(request, 'core/quote.html', {'result': result})
