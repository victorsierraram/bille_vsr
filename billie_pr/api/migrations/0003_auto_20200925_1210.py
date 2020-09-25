# Generated by Django 3.1.1 on 2020-09-25 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_factura'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='products',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='user',
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.producto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='factura',
            name='purchases',
            field=models.ManyToManyField(to='api.Compra'),
        ),
    ]
