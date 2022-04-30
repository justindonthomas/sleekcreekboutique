from django.urls import include
from django.urls import path
from . import views

app_name = 'saleslog'
urlpatterns = [
    path('', views.index, name='index'),
    path('view_listings/', views.view_listings, name='view_listings'),
    path('add_listing/', views.add_listing, name='add_listing'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('edit_character_name_submit/', views.edit_character_name_submit, name='edit_character_name_submit'),
    path('edit_guilds_submit/', views.edit_guilds_submit, name='edit_guilds_submit'),
    path('add_listing_submit/', views.add_listing_submit, name='add_listing_submit'),
]