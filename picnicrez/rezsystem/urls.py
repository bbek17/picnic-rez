from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('FAQ/', views.FAQ, name ='FAQ' ),
    path('Rules/', views.rules, name='rules'),
    path('Maps/', views.maps, name='maps')
]