from django.db import models

# Create your models here.

class Stock(models.Model):
    category = models.CharField(max_length=50, blank=False, null=True)
    item_name = models.CharField(max_length=50, blank=False, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    received_quantity = models.IntegerField(default='0', blank=True, null=True)
    received_by = models.CharField(max_length=50, blank=True, null=True)
    issued_quantity = models.IntegerField(default='0', blank=True, null=True)
    issued_by = models.CharField(max_length=50, blank=True, null=True)
    issued_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False,  auto_now=True)
    export_to_CSV = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item_name  +  self.quantity
