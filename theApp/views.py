from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponsePermanentRedirect,HttpResponseNotFound
from django.shortcuts import redirect
from . models import URLDATA
import random
import string


def home(request):

    if request.method == 'POST':
        url = request.POST.get('url')
        slug = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))

        if URLDATA.objects.filter(Short_URL=slug).exists():    
            slug = ''.join(random.choice(string.ascii_letters)
                            for x in range(10))
        
        #  Saving the Long And Short_Urls to our Database
        roboly = URLDATA(Long_URL=url,Short_URL=slug)
        roboly.save()
        
        return render(request, 'index.html',{'slug':slug})

    return render(request, 'index.html')

def redirectClient (request,slug):

    try:
        return redirect (URLDATA.objects.get(Short_URL=slug).Long_URL)
    except:
        return HttpResponseNotFound()
