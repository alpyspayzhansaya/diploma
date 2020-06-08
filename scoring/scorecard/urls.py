from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('declined', views.declined, name='declined'),
    path('approved', views.approved, name='approved')
]
