# Generated by Django 3.2.18 on 2023-06-10 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('number', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('communication_method', models.CharField(max_length=30, verbose_name='Способ связи')),
                ('file', models.ImageField(upload_to='consultation/', verbose_name='Эскиз')),
            ],
        ),
    ]