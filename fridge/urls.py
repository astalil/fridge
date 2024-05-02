from django.urls import path
from .views import *

urlpatterns = [
    path("<int:fridge_id>/add-item", AddItemToFridgeView.as_view(), name="add-item"),
    path("invite-people", InvitePeopleView.as_view(), name="add-item"),
    path("new-fridge", AddNewFridgeView.as_view(), name="new-fridge"),
    
]