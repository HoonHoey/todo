# Generated by Django 3.1.1 on 2020-09-04 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteGroup',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('reg_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
