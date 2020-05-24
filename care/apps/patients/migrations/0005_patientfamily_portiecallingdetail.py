# Generated by Django 2.2.11 on 2020-05-24 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import fernet_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0004_patienttimeline'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientFamily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('relation', models.CharField(max_length=55)),
                ('age_month', models.PositiveIntegerField()),
                ('age_year', models.PositiveIntegerField()),
                ('phone_number', models.CharField(max_length=15)),
                ('address', fernet_fields.fields.EncryptedTextField(default='')),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Non-binary')])),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PortieCallingDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('called_at', models.DateTimeField()),
                ('able_to_connect', models.BooleanField(default=True)),
                ('comments', models.TextField(blank=True)),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.Patient')),
                ('patient_family', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.PatientFamily')),
                ('portie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
