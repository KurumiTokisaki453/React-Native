from rest_framework import viewsets
from .serializer import *
from .models import *

class UsuariosView(viewsets.ModelViewSet):
    serializer_class = UsuariosSerializer
    queryset = Usuarios.objects.all()
class CuentasView(viewsets.ModelViewSet):
    serializer_class = CuentasSerializer
    queryset = Cuentas.objects.all()
class SesionesView(viewsets.ModelViewSet):
    serializer_class = SesionesSerializer
    queryset = Sesiones.objects.all()
class PaqueteView(viewsets.ModelViewSet):
    serializer_class = PaqueteSerializer
    queryset = Paquete.objects.all()
class UbicacionView(viewsets.ModelViewSet):
    serializer_class = UbicacionSerializer
    queryset = Ubicacion.objects.all()
class DestinosView(viewsets.ModelViewSet):
    serializer_class = DestinosSerializer
    queryset = Destinos.objects.all()
class UsuariofinalView(viewsets.ModelViewSet):
    serializer_class = UsuariofinalSerializer
    queryset = Usuariofinal.objects.all()
class DestinofinalView(viewsets.ModelViewSet):
    serializer_class = DestinofinalSerializer
    queryset = Destinofinal.objects.all()
class NroseguimientoView(viewsets.ModelViewSet):
    serializer_class = NroseguimientoSerializer
    queryset = Nroseguimiento.objects.all()
class SaveseguimientosView(viewsets.ModelViewSet):
    serializer_class = SaveseguimientosSerializer
    queryset = Saveseguimientos.objects.all()
class AsignacionenvioView(viewsets.ModelViewSet):
    serializer_class = AsignacionenvioSerializer
    queryset = Asignacionenvio.objects.all()
class DestinoinicialView(viewsets.ModelViewSet):
    serializer_class = DestinoinicialSerializer
    queryset = Destinoinicial.objects.all()
class EmpleadosView(viewsets.ModelViewSet):
    serializer_class = EmpleadosSerializer
    queryset = Empleados.objects.all()