# Generated by Django 4.1.2 on 2022-10-25 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Matrix', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nazvanie9models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('shirt_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
            ],
        ),
    ]
