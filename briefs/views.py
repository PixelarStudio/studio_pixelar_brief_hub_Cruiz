from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Brief
from .forms import BriefForm

class BriefListView(ListView):
    model = Brief
    template_name = "briefs/brief_list.html"
    context_object_name = "briefs"

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(title__icontains=q) | qs.filter(client_name__icontains=q)
        return qs

class BriefDetailView(DetailView):
    model = Brief
    template_name = "briefs/brief_detail.html"
    context_object_name = "brief"

class BriefCreateView(LoginRequiredMixin, CreateView):
    model = Brief
    form_class = BriefForm
    template_name = "briefs/brief_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("brief_detail", args=[self.object.pk])

class BriefUpdateView(LoginRequiredMixin, UpdateView):
    model = Brief
    form_class = BriefForm
    template_name = "briefs/brief_form.html"

    def get_success_url(self):
        return reverse_lazy("brief_detail", args=[self.object.pk])

class BriefDeleteView(LoginRequiredMixin, DeleteView):
    model = Brief
    template_name = "briefs/brief_confirm_delete.html"
    success_url = reverse_lazy("brief_list")
