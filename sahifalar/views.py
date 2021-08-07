from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class CoursesPageView(TemplateView):
    template_name = 'courses.html'

class TrainersPageView(TemplateView):
    template_name = 'trainers.html'

class EventsPageView(TemplateView):
    template_name = 'events.html'
