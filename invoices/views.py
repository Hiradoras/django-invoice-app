from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Invoice
from profiles.models import Profile

class InvoiceListView(ListView):
    model = Invoice
    template_name = "invoices/main.html" # default invoice_list.html
    # paginate_by
    context_object_name = 'qs'

    def get_queryset(self):
        # profile = Profile.objects.get(user=self.request.user)
        # With doing this, you can show logged profile only
        profile = get_object_or_404(Profile, user = self.request.user)
        # qs = Invoice.objects.filter(profile=profile).order_by("-created")
        # return qs
        return super().get_queryset().filter(profile=profile).order_by('-created')
