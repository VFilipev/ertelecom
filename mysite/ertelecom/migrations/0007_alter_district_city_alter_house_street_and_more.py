# Generated by Django 5.1.1 on 2024-09-17 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ertelecom', '0006_rename_name_city_label_rename_name_district_label_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nodes', to='ertelecom.city'),
        ),
        migrations.AlterField(
            model_name='house',
            name='street',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nodes', to='ertelecom.street'),
        ),
        migrations.AlterField(
            model_name='street',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nodes', to='ertelecom.district'),
        ),
    ]
