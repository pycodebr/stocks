from django.urls import path
from . import views


urlpatterns = [
    path('stocks/', views.StockPriceView.as_view(), name='get_stock_price'),
]
