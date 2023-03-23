from django.urls import path
from . import views

urlpatterns = [
    path('shorturl/', views.geturls, name='shorturls'),
    path('analytics/', views.analytics, name='analytics')
    path('analytics/<int:id>/', views.analytics, name='analytics')

]