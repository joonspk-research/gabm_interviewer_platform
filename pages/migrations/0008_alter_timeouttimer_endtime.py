# Generated by Django 4.2.5 on 2024-02-01 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_timeouttimer_cause'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeouttimer',
            name='endtime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]