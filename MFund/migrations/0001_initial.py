# Generated by Django 3.2.3 on 2021-05-28 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schemes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheme_code', models.CharField(max_length=6)),
                ('scheme_short_info', models.CharField(max_length=200)),
                ('scheme_detail_info', models.CharField(max_length=200)),
            ],
        ),
    ]
