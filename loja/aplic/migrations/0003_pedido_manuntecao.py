# Generated by Django 4.2.7 on 2023-11-24 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0002_alter_cliente_options_alter_loja_celular_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='manuntecao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='aplic.manutenção'),
        ),
    ]