# Generated by Django 4.1.7 on 2023-04-27 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='budget',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(max_length=11, null=True),
        ),
    ]