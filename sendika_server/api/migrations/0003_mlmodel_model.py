# Generated by Django 3.2.8 on 2021-10-22 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_mlmodel_predicted_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='mlmodel',
            name='model',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
    ]
