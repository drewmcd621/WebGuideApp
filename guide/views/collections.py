from django.shortcuts import render
from django.http import HttpResponse

from guide.models import Exhibition

def collections_list(request):
    colls = Exhibition.objects.filter(is_live=True)
    context = {'collections': colls}
    return render(request, 'collections.html', context)

def collection(request, uuid, seo):
    coll = Exhibition.objects.filter(uuid=uuid)
    if coll:
        context = {'c': coll.first()}
        return render(request, "collection.html" , context)
    else:
        return HttpResponse("Not Found")