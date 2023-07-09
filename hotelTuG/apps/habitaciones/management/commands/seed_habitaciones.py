import random
from django.core.management.base import BaseCommand
from faker import Faker
from apps.habitaciones.models import Habitacion

fake = Faker()


class Command(BaseCommand):
    help = 'Genera datos falsos para el modelo Habitacion'

    def handle(self, *args, **options):
        tipos_habitacion = ['S', 'D', 'M', 'Su']
        cantidad = options['cantidad'] if 'cantidad' in options else 10

        for _ in range(cantidad):
            numero = random.randint(1, 9999)
            piso = random.randint(1, 20)
            precio = random.uniform(50, 200)
            estado = random.choice([True, False])
            descripcion = fake.sentence(nb_words=6)
            tipo = random.choice(tipos_habitacion)

            habitacion = Habitacion(
                numero=numero,
                piso=piso,
                precio=precio,
                estado=estado,
                descripcion=descripcion,
                tipo=tipo
            )
            habitacion.save()

        self.stdout.write(self.style.SUCCESS(
            'Datos falsos generados correctamente'))
