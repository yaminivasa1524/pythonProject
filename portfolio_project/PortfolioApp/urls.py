from . import views
from django.urls import path
urlpatterns=[
    path('',views.home, name='home'),
    path('help/',views.help, name='help'),
]
