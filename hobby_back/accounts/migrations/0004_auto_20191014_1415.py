# Generated by Django 2.2.6 on 2019-10-14 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_group_postonetone_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postonetone',
            name='answer',
            field=models.TextField(blank=True),
        ),
    ]
