# Generated by Django 3.0.2 on 2020-01-10 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninjas', '0001_initial'),
        ('professores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='ninjas',
            field=models.ManyToManyField(to='ninjas.Ninja'),
        ),
    ]