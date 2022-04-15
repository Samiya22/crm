from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from . import models
from .forms import *


def leads_lists(request):

    leads = models.Lead.objects.all()

    context = {
      "leads": leads
    }
    return render(request, "leads_lists.html", context)

def lead_detail(request, pk):
   lead = get_object_or_404(models.Lead, id=pk)

   context = {
      "lead": lead
   }
   return render(request, "detailes.html", context)


def lead_create(request):
   print(request.POST)
   context = {
      "forms": LeadForm()
   }
   return render(request, "create.html", context)