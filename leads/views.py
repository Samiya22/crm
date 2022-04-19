from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models
from .forms import *

class SignupView(CreateView):
   template_name = "registration/signup.html"
   form_class = NewUserForm

   def get_success_url(self):
      return reverse('leads:listlar')

class HomeView(TemplateView):
   template_name = "home.html"

class ListsView(LoginRequiredMixin, ListView):
   template_name = "leads_lists.html"
   queryset =  models.Lead.objects.all()
   context_object_name = "leads"


class LeadDetailView(LoginRequiredMixin, DetailView):
   template_name = "details.html"
   queryset =  models.Lead.objects.all()
   context_object_name = "lead"


class LeadCreateView(LoginRequiredMixin, CreateView):
   template_name = "leads/create.html"
   form_class = LeadModelForm

   def get_success_url(self):
      return reverse('leads:listlar')



class LeadUpdateView(LoginRequiredMixin, UpdateView):
   template_name = "leads/update.html"
   form_class = LeadModelForm
   queryset =  models.Lead.objects.all()
   
   def get_success_url(self):
      return reverse('leads:listlar')


def lead_update(request, pk):
   lead = models.Lead.objects.get (id=pk)
   form = LeadModelForm(instance=lead)
   if request.method == "POST":
      form = LeadModelForm(request.POST, instance=lead)
      if form.is_valid():
         form.save()
         return redirect("/leads")
   context = {
      "form": form,
      "lead": lead
   }
   return render(request, "update.html", context)


class LeadDeleteView(LoginRequiredMixin, DeleteView):
   template_name = "leads/delete.html"
   form_class = LeadModelForm
   queryset =  models.Lead.objects.all()

   def get_success_url(self):
      return reverse('leads:listlar')


