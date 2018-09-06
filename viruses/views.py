from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from.models import Virus

def home(request):
    v = Virus.objects.all()
    #return HttpResponse('<p>home view</p>')
    return render(request, 'home.html', {'viruses': v})
    

def dashboard(request, id):
    #return HttpResponse('<p>dashboard view</p>')
    try:
        virus = Virus.objects.get(id=id)
    except Virus.DoesNotExist:
        raise Http404('Virus not found')
    #return render(request, 'dashboard.html', {'virus': virus}) 


def burtin(request):
	return render(request, 'burtin.html', {'Virus': Virus})



    #return render(request, 'virus_detail.html', {'Virus': Virus})

