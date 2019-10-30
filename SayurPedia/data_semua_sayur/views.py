from django.shortcuts import render

from .models import Add_Sayur

# Create your views here.
def index(request):

	Sayur = Add_Sayur.objects.all()

	context = {
		'judul':'Data Sayur ',
		'heading':'Ini About',
		'salam':'Apa yang Anda Cari?',
		'Sayur': Sayur,
	}
	return render(request, 'data_semua_sayur/index.html', context)