# Generated by Django 2.2.11 on 2020-05-31 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0017_auto_20200531_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpatient',
            name='native_country',
            field=models.CharField(blank=True, max_length=56, null=True),
        ),
        migrations.AddField(
            model_name='historicalpatient',
            name='native_state',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='native_country',
            field=models.CharField(blank=True, max_length=56, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='native_state',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='historicalpatient',
            name='phone_number_belongs_to',
            field=models.IntegerField(choices=[(1, 'Self'), (2, 'Father'), (3, 'Mother'), (4, 'Sibling'), (5, 'Spouse'), (6, 'Son'), (7, 'Daughter'), (8, 'Friend'), (9, 'Other relative')], default=1),
        ),
        migrations.AlterField(
            model_name='historicalpatient',
            name='pincode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone_number_belongs_to',
            field=models.IntegerField(choices=[(1, 'Self'), (2, 'Father'), (3, 'Mother'), (4, 'Sibling'), (5, 'Spouse'), (6, 'Son'), (7, 'Daughter'), (8, 'Friend'), (9, 'Other relative')], default=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='pincode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
