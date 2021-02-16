from django.http import HttpResponse

# simplemente creamos una vista, creando una funcion.
# A cada funcion le corresponde un response, es decir cada vista devuelve una respuesta.    
#Hay que enlazar Vista, con URL, linkea en el archivo urls.py
def saludo (request) :
    #""" para saltar linea 
    plantilla = """
    <html>
    <body>
    <div>
    <h1>Holaaaaaaaa</h1>
    </div>
    </body>
    </html>
    """
    return HttpResponse(plantilla)

def caclularEdad(request,anio,edad):

    periodo = anio - 2021
    edadFutura = periodo + edad
    plantilla = "<html><body><h1>En el año %i voy a tener %i</body></html>"%(anio,edadFutura)
    return HttpResponse(plantilla)