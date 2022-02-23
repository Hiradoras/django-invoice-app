from django.urls import path
from .views import InvoiceListView

app_name = 'invoices'

urlpatterns = [
    path('', InvoiceListView.as_view(),name = 'main'),
]
