from django.contrib import admin

<<<<<<< HEAD
from .forms import StockCreateForm

=======
>>>>>>> 87bb5edb326c584cbbae24757dca6d006e18860b
from .models import Stock

# Register your models here.

<<<<<<< HEAD
class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'issued_by', 'quantity']
    form = StockCreateForm
    list_filter = ['category']
    search_fields = ['category', 'item_name']

admin.site.register(Stock, StockCreateAdmin)
=======
admin.site.register(Stock)
>>>>>>> 87bb5edb326c584cbbae24757dca6d006e18860b


