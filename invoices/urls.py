from django.urls import path
from .views import InvoiceFromView, InvoiceListView, InvoiceForm

app_name = 'invoices'

urlpatterns = [
    path('', InvoiceListView.as_view(),name = 'main'),
    path('new/', InvoiceFromView.as_view(), name='create'),
]
