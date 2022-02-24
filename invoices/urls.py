from django.urls import path
from .views import InvoiceFromView, InvoiceListView, InvoiceForm, SimpleTemplateView

app_name = 'invoices'

urlpatterns = [
    path('', InvoiceListView.as_view(),name = 'main'),
    path('new/', InvoiceFromView.as_view(), name='create'),
    path('<pk>/', SimpleTemplateView.as_view(),name='simple-template'),
]
