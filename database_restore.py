import subprocess
import os
import django
from django.conf import settings

# Configurar el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_web.settings")
django.setup()


def restaurar_respaldo():
    # Obtener los parámetros de configuración de la base de datos desde settings.py
    print("Obteniendo configuración de la base de datos...")
    db_settings = settings.DATABASES["default"]
    db_name = db_settings["NAME"]
    db_user = db_settings["USER"]
    db_host = db_settings["HOST"]
    db_port = db_settings["PORT"]
    db_password = db_settings["PASSWORD"]

    print("Configuración obtenida:")
    print(f"  Nombre de la base de datos: {db_name}")
    print(f"  Usuario: {db_user}")
    print(f"  Host: {db_host}")
    print(f"  Puerto: {db_port}")

    # Especificar la ruta del archivo de respaldo
    backup_dir = "C:/backups/"  # Ajusta esta ruta a tu directorio de destino
    backup_file = (
        f"{backup_dir}dbrepsan_backup.sql"  # Ruta del archivo de respaldo específico
    )

    print(f"Archivo de respaldo esperado en: {backup_file}")

    # Verificar si el archivo de respaldo existe
    if not os.path.isfile(backup_file):
        print(f"ERROR: El archivo de respaldo '{backup_file}' no existe.")
        return

    # Establecer la variable de entorno para la contraseña (si es necesario)
    os.environ["PGPASSWORD"] = db_password
    print("Variable de entorno PGPASSWORD configurada.")

    # Comando para restaurar la base de datos con psql
    restore_command = [
        r"C:\Program Files\PostgreSQL\16\bin\psql.exe",  # Ruta a psql
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

    print("Comando a ejecutar:")
    print(f"  {' '.join(restore_command)}")

    try:
        # Ejecutar el comando psql para restaurar la base de datos
        result = subprocess.run(
            restore_command, check=True, capture_output=True, text=True
        )
        print(f"Restauración exitosa desde el archivo: {backup_file}")
        print("Salida del comando:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("ERROR: Falló la restauración de la base de datos.")
        print("Detalles del error:")
        print(e.stderr)
    except FileNotFoundError as fnf_error:
        print("ERROR: No se pudo encontrar el ejecutable de psql.")
        print(f"Detalles del error: {fnf_error}")


# Llamar a la función para restaurar el respaldo
restaurar_respaldo()
