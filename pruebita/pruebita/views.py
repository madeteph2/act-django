from contextvars import Context
from re import template
from xml.dom.minidom import Document
from django.http import HttpResponse
from django.template import Template, Context

def inicio (request):
    
    doc_externo = open ("static/index.html")
    plt = Template (doc_externo.read())
    doc_externo.close()
    ctx = Context()
    Document=plt.render(ctx)
    return HttpResponse(Document)
    