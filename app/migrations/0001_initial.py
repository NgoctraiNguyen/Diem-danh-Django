# Generated by Django 4.2 on 2023-07-13 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staffs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('classroom', models.CharField(max_length=200, null=True)),
                ('phonenumber', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
