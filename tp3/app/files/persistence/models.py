from tortoise.models import Model
from tortoise import fields
from app.auth.persistence.models import User  # Relación con el modelo de usuarios

class File(Model):
    id = fields.IntField(pk=True)  # Clave primaria
    name = fields.CharField(max_length=255)  # Nombre del archivo
    content = fields.TextField(null=True)  # Contenido del archivo (opcional)
    owner = fields.ForeignKeyField(
        "models.User", related_name="files", on_delete=fields.CASCADE
    )  # Relación con el usuario propietario del archivo
    created_at = fields.DatetimeField(auto_now_add=True)  # Fecha de creación
    updated_at = fields.DatetimeField(auto_now=True)  # Fecha de última actualización

    class Meta:
        table = "files"  # Nombre de la tabla en la base de datos
