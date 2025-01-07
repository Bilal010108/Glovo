# Generated by Django 5.1.4 on 2025-01-06 19:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madrid', '0007_alter_userprofile_user_role_storeimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='courierreview',
            name='comment_courier',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='courierreview',
            name='courier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courier_revieww', to='madrid.courier'),
        ),
    ]
