from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Gig, Company, Role
from .forms import GigForm


class GigListView(ListView):
    model = Gig
    template_name = 'gig_list.html'

class GigCreateView(CreateView):
    model = Gig
    form_class = GigForm
    template_name = 'gig_form.html'

class GigUpdateView(UpdateView):
    model = Gig
    form_class = GigForm
    template_name = 'gig_form.html'

class GigDeleteView(DeleteView):
    model = Gig
    success_url = reverse_lazy('gig_list')
    template_name = 'gig_confirm_delete.html'

class GigDetailView(DetailView):
    model = Gig
    template_name = 'gig_detail.html'

