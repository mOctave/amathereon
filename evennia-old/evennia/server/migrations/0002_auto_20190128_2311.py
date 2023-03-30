# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-28 23:11

from base64 import b64encode
from copy import deepcopy
from pickle import dumps, loads

from django.db import migrations

import evennia.utils.picklefield
from evennia.utils.utils import to_bytes


def forwards(apps, schema_editor):
    ServerConfig = apps.get_model("server", "ServerConfig")
    for conf in ServerConfig.objects.all():
        # picklefield requires base64 encoding
        value = loads(to_bytes(conf.db_value), encoding="bytes")  # py2->py3 byte encoding
        conf.db_value = b64encode(dumps(deepcopy(value), protocol=4)).decode()
        conf.save(update_fields=["db_value"])


class Migration(migrations.Migration):

    dependencies = [("server", "0001_initial")]

    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="serverconfig",
            name="db_value",
            field=evennia.utils.picklefield.PickledObjectField(
                help_text="The data returned when the config value is accessed. Must be written as a Python literal if editing through the admin interface. Attribute values which are not Python literals cannot be edited through the admin interface.",
                null=True,
                verbose_name="value",
            ),
        ),
    ]