# Generated by Django 2.1.7 on 2019-02-24 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrmgmt', '0005_auto_20190224_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
