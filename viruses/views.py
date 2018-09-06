from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from.models import Virus

def home(request):
    v = Virus.objects.all()
    #return HttpResponse('<p>home view</p>')
    return render(request, 'home.html', {'viruses': v})



def dashboard(request, id):
    try:
        virus = Virus.objects.get(id=id)
    except Virus.DoesNotExist:
        raise Http404('Virus not found')
    return render(request, 'dashboard.html', {'virus': virus, 'next': (int(id) + 1), 'prev': (int(id) - 1)})



    #return HttpResponse('<p>dashboard view id:{}</p>'.format(id))
    #return render(request, 'virus_detail.html', {'Virus': Virus})
