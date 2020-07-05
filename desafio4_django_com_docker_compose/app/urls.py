from django.urls import path
from app.views import aula_list, aula_create

urlpatterns = [
	path('maratona/', aula_list),
	path('aula_create/', aula_create)
]