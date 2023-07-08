# Generated by Django 4.2.3 on 2023-07-08 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.DecimalField(decimal_places=0, max_digits=4)),
                ('piso', models.DecimalField(decimal_places=0, max_digits=2)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.BooleanField(default=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('tipo', models.CharField(choices=[('S', 'Simple'), ('D', 'Doble'), ('M', 'Matrimonial'), ('Su', 'Suite')], max_length=2)),
            ],
            options={
                'verbose_name': 'Habitacion',
                'verbose_name_plural': 'Habitaciones',
                'db_table': 'habitaciones',
                'ordering': ['piso', 'numero'],
            },
        ),
    ]
