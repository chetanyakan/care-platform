# Generated by Django 2.2.11 on 2020-06-02 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_care_platform'),
        ('patients', '0018_care_platform'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpatient',
            name='city',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='accounts.City'),
        ),
        migrations.AddField(
            model_name='patient',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.City'),
        ),
        migrations.AddField(
            model_name='patientfamily',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.City'),
        ),
        migrations.AlterField(
            model_name='patienttransfer',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Pending'), (2, 'Accepted'), (3, 'Rejected'), (4, 'Withdraw')], default=1),
        ),
    ]
