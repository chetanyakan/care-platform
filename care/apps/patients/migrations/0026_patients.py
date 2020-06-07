# Generated by Django 2.2.11 on 2020-06-07 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0025_auto_20200606_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpatient',
            name='native_state',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='accounts.State'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='native_state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='native_state', to='accounts.State'),
        ),
        migrations.AlterField(
            model_name='patientfacility',
            name='patient_facility_id',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='patientfacility',
            unique_together=set(),
        ),
    ]
