# Generated by Django 3.2.8 on 2021-10-15 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLDATA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Long_URL', models.CharField(max_length=250)),
                ('Short_URL', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
