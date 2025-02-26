import subprocess
import os
import django
from django.conf import settings

# Configurar el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_web.settings")
django.setup()


def hacer_respaldo():
    # Obtener los parámetros de configuración de la base de datos desde settings.py
    db_settings = settings.DATABASES["default"]
    db_name = db_settings["NAME"]
    db_user = db_settings["USER"]
    db_host = db_settings["HOST"]
    db_port = db_settings["PORT"]
    db_password = db_settings["PASSWORD"]

    # Especificar la carpeta donde se guardará el respaldo
    backup_dir = "C:/backups/"  # Ajusta esta ruta a tu directorio de destino

    # Crear un nombre fijo para el archivo de respaldo
    backup_file = f"{backup_dir}{db_name}_backup.sql"

    # Establecer la variable de entorno para la contraseña (si es necesario)
    os.environ["PGPASSWORD"] = db_password

    # Comando pg_dump para crear la copia de seguridad
    pg_dump_command = [
        r"C:\Program Files\PostgreSQL\16\bin\pg_dump.exe",  # Ruta completa a pg_dump
        "-U",
        db_user,
        "-h",
        db_host,
        "-p",
        str(db_port),
        "-d",
        db_name,
        "-f",
        backup_file,
    ]

    try:
        # Ejecutar el comando pg_dump
        subprocess.run(pg_dump_command, check=True)
        print(f"Copia de seguridad realizada con éxito en: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error al realizar la copia de seguridad: {e}")


# Llamar a la función para hacer el respaldo
hacer_respaldo()
