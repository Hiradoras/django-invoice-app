from django.shortcuts import render
from invoices.models import Invoice


def hello_world(request):
    obj = Invoice.objects.get(id=1)
    qs = Invoice.objects.all()
    print(obj.__dict__)
    print("******")
    print(qs.query)
    context = {
        'obj_' : obj, 
        'qs' : qs # <- object_list
        }
    return render(request, 'home.html', context)
