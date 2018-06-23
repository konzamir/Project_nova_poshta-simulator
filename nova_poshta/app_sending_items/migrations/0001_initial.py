# Generated by Django 2.0.6 on 2018-06-23 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(default=0)),
                ('order_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Punkt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=255)),
                ('location_x', models.FloatField(default=0)),
                ('location_y', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transporting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_leaving', models.DateTimeField()),
                ('punkt_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transporting_punkt_from', to='app_sending_items.Punkt')),
                ('punkt_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transporting_punkt_to', to='app_sending_items.Punkt')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('speed', models.IntegerField()),
                ('max_weight', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='transporting',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transporting_vehicle', to='app_sending_items.Vehicle'),
        ),
        migrations.AddField(
            model_name='order',
            name='getter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Order_getter', to='app_sending_items.User'),
        ),
        migrations.AddField(
            model_name='order',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Order_sender', to='app_sending_items.User'),
        ),
        migrations.AddField(
            model_name='order',
            name='transporting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Order_transporting', to='app_sending_items.Transporting'),
        ),
    ]