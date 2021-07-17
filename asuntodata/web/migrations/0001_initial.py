# Generated by Django 3.2 on 2021-04-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('avgPrice', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
