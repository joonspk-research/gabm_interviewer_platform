# Generated by Django 4.2.5 on 2024-01-24 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_participant_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='pruned_p_notes',
            field=models.TextField(default=''),
        ),
    ]