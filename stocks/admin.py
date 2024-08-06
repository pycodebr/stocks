from django.contrib import admin
from stocks.models import Stock


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'moment',)
    search_fields = ('name',)
    list_filter = ('name',)
