# Generated by Django 2.2.2 on 2019-07-13 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbankapp', '0010_brequests_the_donors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brequests',
            name='the_donors',
            field=models.CharField(default='', max_length=700),
        ),
    ]
