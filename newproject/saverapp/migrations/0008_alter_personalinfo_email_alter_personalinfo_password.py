# Generated by Django 5.1.4 on 2024-12-18 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saverapp', '0007_alter_personalinfo_email_alter_personalinfo_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='personalinfo',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
