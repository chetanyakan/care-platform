# Generated by Django 2.2.11 on 2020-05-31 04:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200531_0005'),
        ('patients', '0013_auto_20200531_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpatient',
            name='pincode',
            field=models.CharField(blank=True, max_length=6, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,6}$')]),
        ),
        migrations.AddField(
            model_name='patient',
            name='pincode',
            field=models.CharField(blank=True, max_length=6, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,6}$')]),
        ),
        migrations.AddField(
            model_name='patientfamily',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='patientfamily',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patientfamily',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.District'),
        ),
        migrations.AddField(
            model_name='patientfamily',
            name='pincode',
            field=models.CharField(blank=True, max_length=6, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,6}$')]),
        ),
        migrations.AddField(
            model_name='patientfamily',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.State'),
        ),
        migrations.AddField(
            model_name='patientfamily',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.District'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.State'),
        ),
    ]
