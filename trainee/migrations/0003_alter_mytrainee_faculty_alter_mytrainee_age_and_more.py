# Generated by Django 4.2.1 on 2023-06-02 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0002_mytrainee_appreciation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytrainee',
            name='Faculty',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='mytrainee',
            name='age',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='mytrainee',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
