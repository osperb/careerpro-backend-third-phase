# Generated by Django 4.1.3 on 2022-12-28 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_full_name_alter_account_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(blank=True, default='student', max_length=30, null=True),
        ),
    ]