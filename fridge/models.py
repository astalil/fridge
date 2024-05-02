from django.db import models
from account.models import User

# Create your models here.
class Timestampable (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Fridge(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='owned_fridges')
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='fridges', blank=True)

    def __str__(self):
        return self.name
       
class Item(Timestampable):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    fridge = models.ForeignKey(Fridge, on_delete=models.DO_NOTHING, related_name='items')
    expiry_date = models.DateTimeField()
    image = models.ImageField(upload_to ='uploads/', blank=True, null=True)

    def __str__(self):
        return self.name

class Invitation(models.Model):
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='sent_invitations')
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='received_invitations')
    fridge = models.ForeignKey(Fridge, on_delete=models.DO_NOTHING, related_name='invitations')
    accepted = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.sender.email