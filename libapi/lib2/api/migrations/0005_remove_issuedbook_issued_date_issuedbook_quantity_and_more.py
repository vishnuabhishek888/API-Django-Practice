# Generated by Django 4.1.7 on 2023-03-29 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_issuedbook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issuedbook',
            name='issued_date',
        ),
        migrations.AddField(
            model_name='issuedbook',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='library',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
