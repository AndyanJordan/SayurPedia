from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'judul':'Cari Sayur ',
		'heading':'Ini About',
		'salam':'Apa yang Anda Cari?',
	}
	return render(request, 'search_sayur/index.html', context)