# Generated by Django 5.2.4 on 2025-07-30 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer360', '0002_customer_social_media_alter_interaction_channel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='channel',
            field=models.CharField(choices=[('phone', 'Phone'), ('sms', 'SMS'), ('email', 'Email'), ('letter', 'Letter'), ('social_media', 'Social Media')], max_length=12),
        ),
    ]
