from multiprocessing import context 
from django.shortcuts import get_object_or_404, render, redirect
from . import models
from .forms import *
from pyexpat import model


def home(request):
   return render (request, "home.html")


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
   form = LeadModelForm()
   if request.method == "POST":
      form = LeadModelForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect("/leads")
   context = {
      "forms": form
   }
   return render(request, "create.html", context)


def lead_update(request, pk):
   lead = models.Lead.objects.get (id=pk)
   form = LeadModelForm(instance=lead)
   if request.method == "POST":
      form = LeadModelForm(request.POST, instance=lead)
      if form.is_valid():
         ismi = form.cleaned_data["ismi"]
         familyasi = form.cleaned_data["familyasi"]
         yoshi = form.cleaned_data["yoshi"]
         lead.ismi = ismi
         lead.familyasi = familyasi
         lead.yoshi = yoshi
         form.save()
         return redirect("/leads")

   context = {
      "form": form,
      "lead": lead
   }
   return render(request, "update.html", context)


def lead_delete(request, pk):
   lead = models.Lead.objects.get (id=pk)
   lead.delete()
   return redirect("/leads")
