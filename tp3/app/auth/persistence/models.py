from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)  # Clave primaria
    email = fields.CharField(max_length=255, unique=True)  # Email único
    password = fields.CharField(max_length=255)  # Contraseña encriptada
    created_at = fields.DatetimeField(auto_now_add=True)  # Fecha de creación
    updated_at = fields.DatetimeField(auto_now=True)  # Fecha de última actualización

    class Meta:
        table = "users"  # Nombre de la tabla en la base de datos
