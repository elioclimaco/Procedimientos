from django.db import models


class Procedimiento(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion


class ObjetoContratacion(models.Model):
    procedimiento = models.ForeignKey(Procedimiento, on_delete=models.CASCADE, default=lambda: Procedimiento.objects.get(id=1))
    OBJETOS_CONTRATACION = (
        ('BIEN', 'Bienes'),
        ('SERV', 'Servicios'),
        ('OBRA', 'Obras'),
    )
    descripcion = models.CharField(max_length=200, choices=OBJETOS_CONTRATACION, default=OBJETOS_CONTRATACION[0][0])
    OPERADORES = (
        ('MYRQ', '>'),
        ('MYRI', '>='),
        ('MNRQ', '>'),
        ('MNRI', '<='),
        ('IUAL', '='),
    )
    operador_inicial = models.CharField(max_length=50, choices=OPERADORES, default=OPERADORES[0][0])
    monto_inicial = models.DecimalField(max_digits=9, decimal_places=2)
    operador_final = models.CharField(max_length=50, choices=OPERADORES, default=OPERADORES[0][0])
    monto_final = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.get_descripcion_display()