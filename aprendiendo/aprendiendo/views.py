from django.http import HttpResponse
import datetime
from django.shortcuts import render
from django.template import Template, Context
# primera vista

def template (param):
    return f'<h1> hola, {param}! </h1>'


def index(request):
    nombre = 'julian'
    return HttpResponse(template(nombre))

def despedida(request):
    return HttpResponse('Nos vemos, campeón!')

def dameFecha(request):
    fecha_actual = datetime.datetime.now()
    template = """
    <h1>
    La fecha actual es:
    <span id="fecha">{fecha_actual}</span>
    </h1>

    <script>
    function actualizarFecha() {
        var fechaElemento = document.getElementById('fecha');
        var fechaActual = new Date();
        fechaElemento.textContent = fechaActual;
    }


    setInterval(actualizarFecha, 1000);
    </script>
    """

    return HttpResponse(template)

def calculaEdad(request, edad, anio):
    edadActual = edad
    periodo = anio - 2023
    edadFutura = edadActual + periodo
    documento = f'<h1 style="color: red">tendras {edadFutura} años</h1>'

    return HttpResponse(documento)


def sitio(request):
    sitio_web = open('C:/Users/julia/OneDrive/Escritorio/django/aprendiendo/aprendiendo/plantillas/app.html')
    template = Template(sitio_web.read())
    sitio_web.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)
