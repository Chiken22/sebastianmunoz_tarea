
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from family.models import Family


# Create your views here.
def create_family(request, name: str, last_name: str):

    template = loader.get_template("template_family.html")

    family = Family(name=name, last_name=last_name)
    family.save()  # save into the DB

    context_dict = {"family": family}
    render = template.render(context_dict)
    return HttpResponse(render)

