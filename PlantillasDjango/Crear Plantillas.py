import confi_plantillas as confi
import random as rd
# lista = ["Usuarios",
#          "Cuentas",
#          "Sesiones",
#          "Paquete",
#          "Ubicacion",
#          "Destinos",
#          "UsuarioFinal",
#          "destinofinal",
#          "nroSeguimiento",
#          "saveSeguimientos",
#          "AsignacionEnvio",
#          "DestinoInicial",
#          "Empleados"]

lineas_con_texto = []
texto_minusculas = []
def lista_a_minusculas(lineas_con_texto, imprimir=""):
  texto_minusculas = [elemento.lower() for elemento in lineas_con_texto]
  if imprimir == "print":
    for i in texto_minusculas:
      print(i)
  return texto_minusculas

def nombrePropio(lista_minuscula):
  newlista=[]
  for texto in lista_minuscula:
    newlista.append(confi.mayuscula01(texto))
  return newlista

def lista_no_modelspy(nombre_archivo,texto):
  try:
    with open(nombre_archivo, 'r') as archivo:
      for linea in archivo: # Elimina blancos al inicio y al final de la línea
        linea = linea.strip()    
        # Verifica si la línea comienza con "texto"
        if linea.startswith(texto):
          sin_class=linea[6:]
          sin_models=sin_class[:-15]
          lineas_con_texto.append(sin_models)
  except FileNotFoundError:
    return f"El archivo '{nombre_archivo}' no se encontró."
  except Exception as e:
    return f"Error al leer el archivo: {str(e)}"
  return lineas_con_texto

def a_lista_tablas_models(imprimir):
    nombre_archivo = "./apirestapp/models.py"
    # nombre_archivo = input("Ingresa el nombre del archivo: ")
    texto = "class"
    contenido_archivo = lista_no_modelspy(nombre_archivo,texto)
    if imprimir=="print":
      for i in contenido_archivo:
        print(i)
    else:
      return contenido_archivo
    # print(contenido_archivo)
    
def b_adminpy_register(lista_modelos):
  print("""from django.contrib import admin
from .models import * """)
  for textoInput in lista_modelos:
    print(f"""admin.site.register({textoInput})""")

def c_serializerpy(lista_modelos):
  print("""from rest_framework import serializers
from .models import *""")
  for texto in lista_modelos:
    print(f"""
class {texto}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {texto}
        fields = '__all__'
""")

def d_crearViewsApp(lista):
  textoInput = ""
  print("""from rest_framework import viewsets
from .serializer import *
from .models import *""")
  for i in lista:
    textoInput = i
    print(f"""class {textoInput}View(viewsets.ModelViewSet):
    serializer_class = {textoInput}Serializer
    queryset = {textoInput}.objects.all()""")

def e_crearView_UrlsSerializado(lista_mayuscula,lista_minuscula):

  for i in range(len(lista_mayuscula)):
    textomayus=lista_mayuscula[i]
    textominus=lista_minuscula[i]
    print(f"""
{textominus} = routers.DefaultRouter()
{textominus}.register(r"apirestapp", views.{textomayus}View, "{textominus}")""")
    
  contador=1
  print("urlpatterns = [")
  for i in range(len(lista_mayuscula)):
    textominus=lista_minuscula[i]
    print(f"""    path("v{i+1}-{textominus}/", include({textominus}.urls)),""")
    contador+=1
  print("]")


def f_lista_de_nombres(lista_random, elementos):
  lista_aleatoria = rd.sample(lista_random, elementos)
  for i in lista_aleatoria:
    print(i)
  return lista_aleatoria
  

a_lista_tablas_models("") # 'print' de entreda para imprimir
texto_minusculas = lista_a_minusculas(lineas_con_texto) # agregar 'print' al igual que el anterior para poder imprimir el resultado
listaModelos = nombrePropio(texto_minusculas)
# b_adminpy_register(listaModelos)
# c_serializerpy(listaModelos)
# d_crearViewsApp(listaModelos)
# e_crearView_UrlsSerializado(listaModelos,texto_minusculas)


# cantidad = 3
# f_lista_de_nombres(texto_minusculas, cantidad)


def z_activar_venv_virtual():
  print(".\pyvirtualvenv\Scripts\activate")
z_activar_venv_virtual()
