from django.urls import include
from django.urls import path
from . import views

app_name = 'saleslog'
urlpatterns = [
    path('', views.index, name='index'),
    path('view_listings/', views.view_listings, name='view_listings'),
    path('add_listing/', views.add_listing, name='add_listing'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('edit_profile_submit/', views.edit_profile_submit, name='edit_profile_submit'),
]