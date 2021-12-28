# Generated by Django 4.0 on 2021-12-28 12:46
import os.path

from django.db import connection, migrations


def create_view(apps, schema_editor):

    with connection.cursor() as cursor:
        import database_size
        with open(os.path.join(database_size.__path__[0], f"sql/table.{connection.vendor}.sql")) as file:
            cursor.execute(file.read())


class Migration(migrations.Migration):

    dependencies = [
        ('database_size', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_view),
    ]
