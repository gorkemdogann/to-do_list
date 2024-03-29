# Generated by Django 3.2 on 2021-04-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={},
        ),
        migrations.AlterField(
            model_name='todo',
            name='complete',
            field=models.BooleanField(default=False, verbose_name='Tamamlandı'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='todo',
            order_with_respect_to='user',
        ),
    ]
