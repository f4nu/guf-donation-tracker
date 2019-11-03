# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-19 05:20


from django.db import migrations, models
import tracker.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0013_add_bid_option_max_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='auto_approve_threshold',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Leave blank to turn off auto-approval behavior. If set, anonymous, no-comment donations at or above this amount get sent to the reader. Below this amount, they are ignored.', max_digits=20, null=True, validators=[tracker.validators.positive], verbose_name='Threshold amount to send to reader or ignore'),
        ),
    ]
