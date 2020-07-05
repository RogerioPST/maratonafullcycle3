from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.views import generic

from .models import Aula


class IndexView(generic.ListView):
    template_name = 'maratona/index.html'
    context_object_name = 'latest_aulas_list'

    def get_queryset(self):
        """Return the last 10 published aulas."""
        return Aula.objects.order_by('live_date')[:10]


class DetailView(generic.DetailView):
    model = Aula
    template_name = 'maratona/detail.html'

