# Generated by Django 2.1.8 on 2019-05-27 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("froide_payment", "0005_auto_20190521_1351"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plan",
            name="interval",
            field=models.PositiveSmallIntegerField(
                blank=True,
                choices=[
                    (1, "monthly"),
                    (3, "quarterly"),
                    (6, "semiannually"),
                    (12, "annually"),
                ],
                null=True,
                verbose_name="interval",
            ),
        ),
    ]
