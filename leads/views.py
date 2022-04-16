from multiprocessing import context
from pyexpat import model
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
   forms = LeadForm()
   if request.method == "POST":
      form = LeadForm(request.POST)
      if form.is_valid():
         print(form.cleaned_data)
         ismi = form.cleaned_data["ismi"]
         familyasi = form.cleaned_data["familyasi"]
         yoshi = form.cleaned_data["yoshi"]
         agent = models.Agent.objects.first()
         models.Lead.objects.create(
            ismi=ismi,
            familyasi=familyasi,
            yoshi=yoshi,
            agent=agent,
         )
         print("Muvoffaqiyat")
   context = {
      "forms": forms
   }
   return render(request, "create.html", context)