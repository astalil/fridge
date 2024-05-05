from django.contrib import admin
from .models import Fridge, Invitation, Item

# Register your models here.
class FridgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')
    search_fields = ('name',)

class InvitationAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'fridge',  'accepted', 'declined')
    list_filter = ('accepted', 'declined')
    search_fields = ('sender',)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'fridge')
    list_filter = ('fridge',)

admin.site.register(Fridge, FridgeAdmin)
admin.site.register(Invitation, InvitationAdmin)
admin.site.register(Item, ItemAdmin)