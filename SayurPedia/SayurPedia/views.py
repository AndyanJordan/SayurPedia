from django.shortcuts import render

def index(request):
	context = {
		'judul':'Sayur Pedia',
	}
	return render(request,'index.html', context)