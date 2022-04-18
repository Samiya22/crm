from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from . import models
from .forms import *

class HomeView(TemplateView):
   template_name = "home.html"

class ListsView(ListView):
   template_name = "leads_lists.html"
   queryset =  models.Lead.objects.all()
   context_object_name = "leads"


class LeadDetailView(DetailView):
   template_name = "details.html"
   queryset =  models.Lead.objects.all()
   context_object_name = "lead"


class LeadCreateView(CreateView):
   template_name = "create.html"
   form_class = LeadModelForm

   def get_success_url(self):
      return reverse('leads:listlar')




# def lead_create(request):
#    form = LeadModelForm()
#    if request.method == "POST":
#       form = LeadModelForm(request.POST)
#       if form.is_valid():
#          form.save()
#          return redirect("/leads")
#    context = {
#       "forms": form
#    }
#    return render(request, "create.html", context)


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
