from django.urls import path
from .views import CloseInvoiceView, InvoiceFromView, InvoiceListView, InvoiceForm, SimpleTemplateView, InvoiceUpdateView, AddPositionsFormView, RedirectView

app_name = 'invoices'

urlpatterns = [
    path('', InvoiceListView.as_view(),name = 'main'),
    path('new/', InvoiceFromView.as_view(), name='create'),
    # path('<pk>/', SimpleTemplateView.as_view(),name='simple-template'),
    path('<pk>/', AddPositionsFormView.as_view(),name='detail'),
    path('<pk>/update', CloseInvoiceView.as_view(),name='close'),
    path('<pk>/update', InvoiceUpdateView.as_view(),name='update'),
    
]
