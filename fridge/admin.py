from django.contrib import admin
from .models import Fridge, Invitation, Item

# Register your models here.
class FridgeAdmin(admin.ModelAdmin):
    pass

class InvitationAdmin(admin.ModelAdmin):
    pass

class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Fridge, FridgeAdmin)
admin.site.register(Invitation, InvitationAdmin)
admin.site.register(Item, ItemAdmin)