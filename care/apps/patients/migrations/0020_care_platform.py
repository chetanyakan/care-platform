# Generated by Django 2.2.11 on 2020-06-04 10:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0019_care_platform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portiecallingdetail',
            name='patient_family',
        ),
        migrations.AddField(
            model_name='portiecallingdetail',
            name='patient_number',
            field=models.CharField(default=1, max_length=14, validators=[django.core.validators.RegexValidator(code='invalid_mobile', message='Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>', regex='^((\\+91|91|0)[\\- ]{0,1})?[456789]\\d{9}$')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portiecallingdetail',
            name='relation',
            field=models.IntegerField(choices=[(2, 'Father'), (3, 'Mother'), (4, 'Sibling'), (5, 'Spouse'), (6, 'Son'), (7, 'Daughter'), (8, 'Friend'), (9, 'Other relative')], default=1),
            preserve_default=False,
        ),
    ]
