from django.db import models

class Horario(models.Model):
    PERIODO = [
        (1, 'Matutino'),
        (2, 'Vespertino'),
        (3, 'Noturno'),
    ]
    
    hora = models.TimeField()
    periodo = models.IntegerField(choices=PERIODO)
