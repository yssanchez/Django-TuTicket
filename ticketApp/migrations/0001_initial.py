# Generated by Django 4.2.5 on 2023-12-02 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conciertos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artista', models.CharField(max_length=50)),
                ('lugar', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('duracion', models.PositiveIntegerField()),
                ('imagen', models.ImageField(upload_to='conciertos')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('precio', models.PositiveIntegerField()),
                ('tickets_disponibles', models.PositiveIntegerField()),
                ('tickets_vendidos', models.PositiveIntegerField()),
                ('concierto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketApp.conciertos')),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('codigo', models.CharField(blank=True, max_length=50)),
                ('entradas', models.PositiveIntegerField()),
                ('total_original', models.PositiveIntegerField(default=0)),
                ('total_descuento', models.PositiveIntegerField(default=0)),
                ('total_final', models.PositiveIntegerField(default=0)),
                ('fecha', models.DateField()),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketApp.show')),
            ],
        ),
    ]