from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from apirestapp import views
# api verioning
usuarios = routers.DefaultRouter()
usuarios.register(r"apirestapp", views.UsuariosView, "usuarios")

cuentas = routers.DefaultRouter()
cuentas.register(r"apirestapp", views.CuentasView, "cuentas")

sesiones = routers.DefaultRouter()
sesiones.register(r"apirestapp", views.SesionesView, "sesiones")

paquete = routers.DefaultRouter()
paquete.register(r"apirestapp", views.PaqueteView, "paquete")

ubicacion = routers.DefaultRouter()
ubicacion.register(r"apirestapp", views.UbicacionView, "ubicacion")

destinos = routers.DefaultRouter()
destinos.register(r"apirestapp", views.DestinosView, "destinos")

usuariofinal = routers.DefaultRouter()
usuariofinal.register(r"apirestapp", views.UsuariofinalView, "usuariofinal")

destinofinal = routers.DefaultRouter()
destinofinal.register(r"apirestapp", views.DestinofinalView, "destinofinal")

nroseguimiento = routers.DefaultRouter()
nroseguimiento.register(r"apirestapp", views.NroseguimientoView, "nroseguimiento")       

saveseguimientos = routers.DefaultRouter()
saveseguimientos.register(r"apirestapp", views.SaveseguimientosView, "saveseguimientos") 

asignacionenvio = routers.DefaultRouter()
asignacionenvio.register(r"apirestapp", views.AsignacionenvioView, "asignacionenvio")    

destinoinicial = routers.DefaultRouter()
destinoinicial.register(r"apirestapp", views.DestinoinicialView, "destinoinicial")       

empleados = routers.DefaultRouter()
empleados.register(r"apirestapp", views.EmpleadosView, "empleados")
urlpatterns = [
    path("v01-usuarios/", include(usuarios.urls)),
    path("v02-cuentas/", include(cuentas.urls)),
    path("v03-sesiones/", include(sesiones.urls)),
    path("v04-paquete/", include(paquete.urls)),
    path("v05-ubicacion/", include(ubicacion.urls)),
    path("v06-destinos/", include(destinos.urls)),
    path("v07-usuariofinal/", include(usuariofinal.urls)),
    path("v08-destinofinal/", include(destinofinal.urls)),
    path("v09-nroseguimiento/", include(nroseguimiento.urls)),
    path("v10-saveseguimientos/", include(saveseguimientos.urls)),
    path("v11-asignacionenvio/", include(asignacionenvio.urls)),
    path("v12-destinoinicial/", include(destinoinicial.urls)),
    path("v13-empleados/", include(empleados.urls)),
    path("docs/", include_docs_urls(title="apirestapp API")),
]