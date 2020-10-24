from django.shortcuts import render

from django.http import HttpResponse


def newcert(request):
        return(render(request,'newcert/newcertform.html'))


# Create your views here.
