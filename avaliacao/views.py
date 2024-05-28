from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse
from .models import Avaliacao, Empresa
from .forms import AvaliacaoForm


#precisa chcar permissões antes de salvar, ler, editar e excluir.

class AvaliacaoListView(ListView):
    model = Avaliacao
    template_name = 'avaliacao_list.html'

class AvaliacaoCreateView(CreateView):
    model = Avaliacao
    form_class = AvaliacaoForm
    template_name = 'avaliacao_form.html'

    def get_success_url(self):
        return reverse('avaliacao:avaliacao-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empresas'] = Empresa.objects.all()
        return context

class AvaliacaoUpdateView(UpdateView):
    model = Avaliacao
    form_class = AvaliacaoForm
    template_name = 'avaliacao_form.html'

    def get_success_url(self):
        return reverse('avaliacao:avaliacao-list')

class AvaliacaoDetailView(DetailView):
    model = Avaliacao
    template_name = 'avaliacao_detail.html'

class AvaliacaoDeleteView(DeleteView):
    model = Avaliacao
    template_name = 'avaliacao_confirm_delete.html'

    def get_success_url(self):
        return reverse('avaliacao:avaliacao-list')
