# Generated by Django 4.2.7 on 2023-11-24 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0005_modelo_alter_celular_options_alter_pedido_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='celular',
            name='celular',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplic.modelo'),
        ),
    ]
