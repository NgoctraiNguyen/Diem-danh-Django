# Generated by Django 4.2 on 2023-07-15 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_event_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acttendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.event')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.staffs')),
            ],
        ),
    ]