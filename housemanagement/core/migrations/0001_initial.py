# Generated by Django 4.2 on 2023-04-03 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counryCode', models.CharField(max_length=3)),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('house', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment', models.CharField(max_length=10)),
                ('square', models.FloatField()),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.house')),
            ],
        ),
    ]