# Generated by Django 4.0 on 2022-04-24 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='memberdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=None)),
                ('phone', models.IntegerField(default=None)),
                ('country', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('mandal', models.CharField(max_length=50)),
                ('village', models.CharField(max_length=50)),
                ('house_no', models.CharField(max_length=50)),
                ('pin_code', models.IntegerField(default=None)),
                ('Near_police_station', models.CharField(max_length=20)),
                ('text_area', models.CharField(max_length=8000)),
            ],
        ),
    ]
