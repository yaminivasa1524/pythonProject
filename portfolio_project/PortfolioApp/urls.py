from . import views
from django.urls import path
urlpatterns=[
    path('', views.home, name='home'),
    path('help', views.help, name='help'),
    path('contact view', views.contact_view, name='contact_view'),
]


