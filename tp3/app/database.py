from tortoise import Tortoise

TORTOISE_ORM = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": "postgres",  # Nombre del servicio del contenedor Docker
                "port": "5432",
                "user": "user",
                "password": "password",
                "database": "tp3_database",
            },
        },
    },
    "apps": {
        "models": {
            "models": [
                "app.auth.persistence.models",
                "app.files.persistence.models",
                "aerich.models",
            ],
            "default_connection": "default",
        },
    },
}


async def init_db():
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()
