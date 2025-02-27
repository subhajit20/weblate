# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.2.5 on 2023-09-13 08:55

import django.db.models.functions.text
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trans", "0188_remove_change_trans_chang_timesta_33178f_idx_and_more"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="unit",
            name="trans_unit_source_md5_index",
        ),
        migrations.RemoveIndex(
            model_name="unit",
            name="trans_unit_target_md5_index",
        ),
        migrations.RemoveIndex(
            model_name="unit",
            name="trans_unit_context_md5_index",
        ),
        migrations.AddIndex(
            model_name="unit",
            index=models.Index(
                django.db.models.functions.text.MD5(
                    django.db.models.functions.text.Lower("source")
                ),
                models.F("translation"),
                name="trans_unit_source_md5",
            ),
        ),
        migrations.AddIndex(
            model_name="unit",
            index=models.Index(
                django.db.models.functions.text.MD5(
                    django.db.models.functions.text.Lower("target")
                ),
                models.F("translation"),
                name="trans_unit_target_md5",
            ),
        ),
        migrations.AddIndex(
            model_name="unit",
            index=models.Index(
                django.db.models.functions.text.MD5(
                    django.db.models.functions.text.Lower("context")
                ),
                models.F("translation"),
                name="trans_unit_context_md5",
            ),
        ),
    ]
