from django.shortcuts import render
from django.views.generic import ListView
from .models import Invoice


class InvoiceListView(ListView):
    model = Invoice
    # template_name = "invoices/main.html" # default invoice_list.html
    # paginate_by
    # context_object_name = 'qs'