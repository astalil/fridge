from django.urls import path
from .views import *

urlpatterns = [
    path("invite-people", InvitePeopleView.as_view(), name="add-item"),
    path("new-fridge", AddNewFridgeView.as_view(), name="new-fridge"),
    path("<int:fridge_id>/add-item", AddItemToFridgeView.as_view(), name="add-item"),
    path("remove-item", RemoveItemFromFridgeView.as_view(), name="remove-items"),
    path("invitations", InvitationsView.as_view(), name="get-invitations"),
    path("invite-action", InviteActionView.as_view(), name="invite-action"),
    path("get-items/<int:fridge_id>", GetItemsView.as_view(), name="pull-items"),
]