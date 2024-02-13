# Generated by Django 5.0 on 2024-02-13 21:23

import tracker.validators
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0035_interview_changes'),
    ]

    operations = [
        migrations.AddField(
            model_name='milestone',
            name='start',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=20, validators=[tracker.validators.positive, tracker.validators.nonzero]),
        ),
    ]