from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.predict, name='valueuno-predict'),
    path('about/', TemplateView.as_view(template_name="valueuno/about.html")),
]