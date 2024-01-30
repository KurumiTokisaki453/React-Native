from django.db import models

# Create your models here.
 
class Usuarios(models.Model):
    idcreador = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=255)
    Apellido = models.CharField(max_length=255, blank=True)
    Nacimiento = models.DateField(blank=True)
    DNI = models.IntegerField()
    Genero = models.BooleanField(blank=True)
    fkcuenta = models.ForeignKey('Cuentas', on_delete=models.CASCADE)
    def __str__(self):
      return self.Nombre + " " + self.Apellido

class Cuentas(models.Model):
    idcuenta = models.AutoField(primary_key=True)
    correo = models.CharField(max_length=255)
    contrasena = models.CharField(max_length=255)
    contrasenaantigua = models.CharField(max_length=255, blank=True )
    def __str__(self):
      return self.correo + " " + self.contrasena

class Sesiones(models.Model):
    idsesion = models.AutoField(primary_key=True)
    fkusuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)
    dispositivo = models.CharField(max_length=255)
    fechainicio = models.DateTimeField()
    def __str__(self):
      return self.fkusuario + " " + self.dispositivo

class Paquete(models.Model):
    idpaquete = models.AutoField(primary_key=True)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    volumen = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    resistencia = models.CharField(max_length=255, blank=True)
    temperatura = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.peso + " " +self.volumen + " " + self.resistencia

class Ubicacion(models.Model):
    idubi = models.AutoField(primary_key=True)
    latitud = models.DecimalField(max_digits=10, decimal_places=6)
    longitud = models.DecimalField(max_digits=10, decimal_places=6)
    nombre = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.latitud + " "+ self.longitud

class Destinos(models.Model):
    idregion = models.AutoField(primary_key=True)
    region = models.CharField(max_length=255)
    provincia = models.CharField(max_length=255)
    distrito = models.CharField(max_length=255)
    nropostal = models.IntegerField(blank=True)
    def __str__(self):
        return self.distrito + " " + self.nropostal

class Usuariofinal(models.Model):
    idtemp = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True)
    apellido = models.CharField(max_length=255, blank=True)
    dni = models.IntegerField()
    fkubi = models.ForeignKey('Ubicacion', on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre + " " + self.apellido + " " + self.dni
    
class Destinofinal(models.Model):
    idfinal = models.AutoField(primary_key=True)
    fkdestino = models.ForeignKey('Destinos', on_delete=models.CASCADE)
    Avenida = models.CharField(max_length=255)
    extra = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.Avenida + " " + self.extra

class Nroseguimiento(models.Model):
    idseguimiento = models.AutoField(primary_key=True)
    fkinicial = models.ForeignKey('destinoinicial', on_delete=models.CASCADE)  # Asegúrate de definir la relación adecuada aquí
    fkfinal = models.ForeignKey('destinofinal', on_delete=models.CASCADE)
    fkpaquete = models.ForeignKey('Paquete', on_delete=models.CASCADE)
    creacion = models.DateField()
    estado = models.IntegerField()
    def __str__(self):
        return self.fkinicial+" "+self.fkfinal+" "+self.fkpaquete + " " + self.estado

class Saveseguimientos(models.Model):
    idsave = models.AutoField(primary_key=True)
    fkusuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)
    fkseguimiento = models.ForeignKey('nroSeguimiento', on_delete=models.CASCADE)
    fkCosto = models.IntegerField()
    def __str__(self):
        return self.fkusuario + " " + self.fkCosto

class Asignacionenvio(models.Model):
    idasignacion = models.AutoField(primary_key=True)
    fkseguimiento = models.ForeignKey('nroSeguimiento', on_delete=models.CASCADE)
    fkTemp = models.ForeignKey('UsuarioFinal', on_delete=models.CASCADE)
    fkempleado = models.ForeignKey('Empleados', on_delete=models.CASCADE)
    def __str__(self):
        return self.fkseguimiento + " " + self.fkempleado

class Destinoinicial(models.Model):
    idInicial = models.AutoField(primary_key=True)
    fkdestino = models.ForeignKey('Destinos', on_delete=models.CASCADE)
    Avenida = models.CharField(max_length=255)
    def __str__(self):
        return self.fkdestino + " " +self.Avenida
    
class Empleados(models.Model):
    idEmpleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    dni = models.IntegerField()
    fkcuenta = models.ForeignKey('Cuentas', on_delete=models.CASCADE)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.nombre + " " + self.apellido + " " + self.dni
