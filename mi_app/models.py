from django.db import models

# Tabla Consultas
class Consultas(models.Model):
    nombre = models.CharField(max_length=200) # Columna nombre (max 200 caracteres)
    email = models.CharField(max_length=200) # Columna email (max 200 caracteres)
    mensaje = models.TextField() # Columna mensaje (texto libre)




















