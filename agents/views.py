from django.views import generic
from django.shortcuts import reverse
from leads.models import Agent
from .mixins import OrganiserAndLoginRequiredMixin
from .forms import AgentModelForm

class AgentListView(OrganiserAndLoginRequiredMixin,generic.ListView):
    template_name = "agents/agents_lists.html"

    def get_queryset(self):
        organisiton = self.request.user.userprofile
        return Agent.objects.filter(organisiton=organisiton)

class AgentCreateView(OrganiserAndLoginRequiredMixin, generic.CreateView):
    template_name = "agents/agents_create.html"
    form_class = AgentModelForm

    def get_success_url(self):
        return reverse("agents:agent-list")
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)

class AgentDetailView(OrganiserAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agents_detail.html"
    context_object_name = "agent"

    def get_queryset(self):
        organisiton = self.request.user.userprofile
        return Agent.objects.filter(organisiton=organisiton)

class AgentUpdateView(OrganiserAndLoginRequiredMixin, generic.UpdateView):
    template_name = "agents/agents_update.html"
    form_class = AgentModelForm

    def get_queryset(self):
        organisiton = self.request.user.userprofile
        return Agent.objects.filter(organisiton=organisiton)

    def get_success_url(self):
        return reverse("agents:agent-list")

class AgentDeleteView(OrganiserAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agents_delete.html"
    context_object_name = "agent"

    def get_queryset(self):
        organisiton = self.request.user.userprofile
        return Agent.objects.filter(organisiton=organisiton)

    def get_success_url(self):
        return reverse("agents:agent-list")