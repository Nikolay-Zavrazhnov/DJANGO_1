# Generated by Django 4.1 on 2022-10-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0008_favoriteadv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='status',
            field=models.TextField(choices=[('OPEN', 'Открыто'), ('CLOSED', 'Закрыто'), ('DRAFT', 'Черновик')], default='OPEN'),
        ),
    ]
