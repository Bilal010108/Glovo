# Generated by Django 5.1.4 on 2025-01-07 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madrid', '0008_courierreview_comment_courier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
