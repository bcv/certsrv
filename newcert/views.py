from django.shortcuts import render

from django.http import HttpResponse


def newcert(request):
    return(render(request,'newcert/newcertform.html',{'exttitle':'New Certificate Page'}))


# Create your views here.
