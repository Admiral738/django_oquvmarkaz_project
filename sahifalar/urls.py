from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, CoursesPageView, TrainersPageView, EventsPageView


urlpatterns = [
    path('', HomePageView.as_view(), name = 'index'),
    path('about/',AboutPageView.as_view(), name = 'about'),
    path('contact/',ContactPageView.as_view(), name = 'contact'),
    path('courses/', CoursesPageView.as_view(), name = 'courses'),
    path('trainers/', TrainersPageView.as_view(), name = 'trainers'),
    path('events/', EventsPageView.as_view(), name = 'events'),
]