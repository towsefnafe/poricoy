# Generated by Django 4.0.6 on 2022-07-07 06:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_portfolio_contacts'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='sent_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
