from django.urls import path
from .views import home , about , contact_list , contact_detail , new_contact , edit_contact , delete_contact

urlpatterns = [
    path('' , home , name="home"),
    path('about/' , about , name="about"),
    path("contacts/" , contact_list , name="liste"),
    path("contacts/<int:id>/" , contact_detail , name="detail"),
    path("contacts/new/" , new_contact , name="new-contact"),
    path("contacts/edit-contact/<int:id>" , edit_contact , name="edit-contact"),
    path("contacts/delete-contact/<int:id>" , delete_contact , name="detele-contact")
]