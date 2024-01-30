# Generated by Django 5.0.1 on 2024-01-17 21:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuentas',
            fields=[
                ('idCuenta', models.AutoField(primary_key=True, serialize=False)),
                ('correo', models.CharField(max_length=255)),
                ('contrasena', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Destinos',
            fields=[
                ('idregion', models.AutoField(primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=255)),
                ('provincia', models.CharField(max_length=255)),
                ('distrito', models.CharField(max_length=255)),
                ('nroPostal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('idpaquete', models.AutoField(primary_key=True, serialize=False)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=10)),
                ('volumen', models.DecimalField(decimal_places=2, max_digits=10)),
                ('resistencia', models.CharField(max_length=255)),
                ('temperatura', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('idubi', models.AutoField(primary_key=True, serialize=False)),
                ('latitud', models.DecimalField(decimal_places=6, max_digits=10)),
                ('longitud', models.DecimalField(decimal_places=6, max_digits=10)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='destinofinal',
            fields=[
                ('idfinal', models.AutoField(primary_key=True, serialize=False)),
                ('Avenida', models.CharField(max_length=255)),
                ('extra', models.CharField(max_length=255)),
                ('fkdestino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apirestapp.destinos')),
            ],
        ),
        migrations.CreateModel(
            name='DistinoInicial',
            fields=[
                ('idInicial', models.AutoField(primary_key=True, serialize=False)),
                ('Avenida', models.CharField(max_length=255)),
                ('fkdestino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apirestapp.destinos')),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('idEmpleado', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('dni', models.IntegerField()),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fkcuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apirestapp.cuentas')),
            ],
        ),
        migrations.CreateModel(
            name='nroSeguimiento',
            fields=[
                ('idSeguimiento', models.AutoField(primary_key=True, serialize=False)),
                ('fkInicial', models.IntegerField()),
                ('creacion', models.DateField()),
                ('estado', models.IntegerField()),
                ('fkFinal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apirestapp.destinofinal')),
                ('fkpaquete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apirestapp.paquete')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioFinal',
            fields=[
                ('idtemp', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('dni', models.IntegerField()),
                ('fkdestinofinal', models.IntegerField()),
                ('fkubi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apirestapp.ubicacion')),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionEnvio',
            fields=[
                ('idAsignacion', models.AutoField(primary_key=True, serialize=False)),
                ('fkempleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apirestapp.empleados')),
                ('fkseguimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apirestapp.nroseguimiento')),
                ('fkTemp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apirestapp.usuariofinal')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('idCreador', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=255)),
                ('Apellido', models.CharField(max_length=255)),
                ('Nacimiento', models.DateField()),
                ('DNI', models.IntegerField()),
                ('Genero', models.BooleanField()),
                ('fkcuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apirestapp.cuentas')),
            ],
        ),
        migrations.CreateModel(
            name='Sesiones',
            fields=[
                ('idSesion', models.AutoField(primary_key=True, serialize=False)),
                ('dispositivo', models.CharField(max_length=255)),
                ('fechaInicio', models.DateTimeField()),
                ('fkusuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apirestapp.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='saveSeguimientos',
            fields=[
                ('idSave', models.AutoField(primary_key=True, serialize=False)),
                ('fkCosto', models.IntegerField()),
                ('fkseguimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apirestapp.nroseguimiento')),
                ('fkusuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apirestapp.usuarios')),
            ],
        ),
    ]
