# Generated by Django 2.2.5 on 2020-05-14 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_teach_course_mr_teach_uname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teach_course_mr',
            name='Teach_id',
        ),
    ]
