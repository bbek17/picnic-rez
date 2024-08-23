from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('FAQ/', views.FAQ, name ='FAQ' )
]