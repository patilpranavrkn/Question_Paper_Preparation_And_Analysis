# Generated by Django 2.2.5 on 2020-05-15 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0007_auto_20200515_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatedqprec',
            name='sample',
            field=models.BinaryField(null=True),
        ),
    ]
