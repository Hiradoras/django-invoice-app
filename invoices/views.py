from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, FormView, TemplateView, DetailView
from .models import Invoice
from profiles.models import Profile
from .forms import InvoiceForm
class InvoiceListView(ListView):
    model = Invoice
    template_name = "invoices/main.html" # default invoice_list.html
    paginate_by = 2
    context_object_name = 'qs'

    def get_queryset(self):
        # profile = Profile.objects.get(user=self.request.user)
        # With doing this, you can show logged profile only
        profile = get_object_or_404(Profile, user = self.request.user)
        # qs = Invoice.objects.filter(profile=profile).order_by("-created")
        # return qs
        return super().get_queryset().filter(profile=profile).order_by('-created')

class InvoiceFromView(FormView):
    form_class = InvoiceForm
    template_name = 'invoices/create.html'
    #success_url = reverse_lazy('invoices:main')
    i_instance = None

    def get_success_url(self):
        return reverse('invoices:simple-template', kwargs={'pk': self.i_instance.pk})

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        instance = form.save(commit=False)
        instance.profile = profile
        form.save()
        self.i_instance = instance
        return super().form_valid(form)

class SimpleTemplateView(DetailView):
    model = Invoice
    template_name = 'invoices/simple_template.html'



# class SimpleTemplateView(TemplateView):
#     template_name = 'invoices/simple_template.html'

