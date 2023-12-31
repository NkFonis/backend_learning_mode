# Generated by Django 4.2.3 on 2023-07-23 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(max_length=255)),
                ('shift', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_number', models.IntegerField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('choosen_time', models.DateField()),
                ('Issue_Brief', models.TextField()),
                ('doc', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='appointment.doctor')),
            ],
        ),
    ]
