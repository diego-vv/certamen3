# Generated by Django 4.2.6 on 2023-11-25 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
