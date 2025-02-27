# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 4.2.3 on 2023-08-04 10:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trans", "0174_adjust_fluent_unit_flags"),
    ]

    operations = [
        migrations.AddField(
            model_name="alert",
            name="details_new",
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name="change",
            name="details_new",
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name="comment",
            name="userdetails_new",
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name="component",
            name="enforced_checks_new",
            field=models.JSONField(
                blank=True,
                default=list,
                help_text="List of checks which can not be ignored.",
                verbose_name="Enforced checks",
            ),
        ),
        migrations.AddField(
            model_name="suggestion",
            name="userdetails_new",
            field=models.JSONField(default=dict),
        ),
    ]
