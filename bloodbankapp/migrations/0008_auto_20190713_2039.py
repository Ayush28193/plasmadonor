# Generated by Django 2.2.2 on 2019-07-13 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbankapp', '0007_auto_20190713_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brequests',
            name='blood_group',
            field=models.CharField(choices=[('O Positive', 'O Positive'), ('O Negative', 'O Negative'), ('A Positive', 'A Positive'), ('A Negative', 'A Negative'), ('B Positive', 'B Positive'), ('B Negative', 'B Negative'), ('AB Positive', 'AB Positive'), ('AB Negative', 'AB Negative')], max_length=50),
        ),
    ]