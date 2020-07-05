from django.forms import ModelForm
from django.shortcuts import render, redirect

#view eh o controller no django
# Create your views here.
from app.models import Aula

def aula_list(request):
	aulas = Aula.objects.all()
	return render(
		request,
		'aula_list.html',
		{
			'aulas': aulas
		}
	)

class AulaForm(ModelForm):
		class Meta:
			model = Aula
			fields = ['title', 'image_url', 'video_url', 'live_date']

def aula_create(request):	
	form = AulaForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/maratona')
	return render(
		request,
		'aula_create.html',
		{
			'form': form
		}
	)