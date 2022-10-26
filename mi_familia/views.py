
from django.http import HttpResponse
from django.template import Template, Context

def myfam(request):
    my_html = open ('C:/Users/DC Monster/Documents/sebastiancruz_proyecto/mi_familia/templates/template_group.html')

    template = Template(
        my_html.read()
        .encode("latin-1")
        .decode(
            "utf-8"
        )  # .encode("latin-1").decode("utf-8") se usa para leer correctamente las tildes o acentos del español en Windows
    )  # Se carga en memoria nuestro documento, template1
    ##OJO importar template y contex, con: from django.template import Template, Context

    my_html.close()  # Cerramos el archivo

    context = Context() 
    render = template.render(context)
    return HttpResponse(render)