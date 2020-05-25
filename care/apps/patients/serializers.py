import datetime

from django.utils.translation import ugettext as _
from rest_framework import serializers as rest_serializers
from rest_framework import exceptions as rest_exceptions
from apps.patients import (
    constants as patient_constants,
    models as patient_models,
)
from apps.facility import models as facility_models


class PatientFacilitySerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = patient_models.PatientFacility
        fields = (
            "patient_status",
            "facility",
            "patient_facility_id",
        )
        read_only_fields = ("facility",)


class PatientListSerializer(rest_serializers.ModelSerializer):
    status = rest_serializers.SerializerMethodField()

    class Meta:
        model = patient_models.Patient
        fields = (
            "id",
            "facility",
            "nearest_facility",
            "name",
            "year",
            "month",
            "gender",
            "phone_number",
            "address",
            "date_of_birth",
            "year_of_birth",
            "nationality",
            "passport_no",
            "aadhar_no",
            "is_medical_worker",
            "blood_group",
            "contact_with_confirmed_carrier",
            "state",
            "district",
            "contact_with_suspected_carrier",
            "estimated_contact_date",
            "past_travel",
            "is_active",
            "countries_travelled_old",
            "countries_travelled",
            "date_of_return",
            "present_health",
            "ongoing_medication",
            "has_SARI",
            "local_body",
            "number_of_aged_dependents",
            "created_by",
            "number_of_chronic_diseased_dependents",
            "patient_search_id",
            "date_of_receipt_of_information",
            "cluster_group",
            "clinical_status_updated_at",
            "portea_called_at",
            "portea_able_to_connect",
            "symptoms",
            "diseases",
            "status",
            "covid_status",
            "current_facility",
        )
        extra_kwargs = {
            "facility": {"required": True},
            "nearest_facility": {"required": True},
            "state": {"required": True},
            "district": {"required": True},
        }
        read_only_fields = (
            "symptoms",
            "diseases",
        )

    def get_status(self, instance):
        if instance.patient_status == patient_constants.FACILITY_STATUS:
            return instance.facility_status
        return instance.patient_status


class PatientGroupSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = patient_models.PatientGroup
        fields = (
            "id",
            "name",
            "description",
            "created_at",
        )
        read_only_fields = ("created_at",)


class CovidStatusSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = patient_models.CovidStatus
        fields = (
            "id",
            "name",
            "description",
        )


class ClinicalStatusSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = patient_models.ClinicalStatus
        fields = (
            "id",
            "name",
            "description",
        )


class PatientStatusSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = patient_models.PatientStatus
        fields = ("id", "name", "description")


class PatientTimeLineSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = patient_models.PatientTimeLine
        fields = (
            "date",
            "description",
        )


class PatientSampleTestSerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = patient_models.PatientSampleTest
        fields = (
            "id",
            "patient",
            "testing_lab",
            "doctor_name",
            "result",
            "date_of_sample",
            "date_of_result",
            "status_updated_at",
        )


class PatientFamilySerializer(rest_serializers.ModelSerializer):
    class Meta:
        model = patient_models.PatientFamily
        fields = (
            "name",
            "relation",
            "age_year",
            "age_month",
            "gender",
            "phone_number"
        )


class PortieCallingDetailSerializer(rest_serializers.ModelSerializer):
    name = rest_serializers.SerializerMethodField()
    portie_phone_number = rest_serializers.SerializerMethodField()
    patient_contact_number = rest_serializers.SerializerMethodField()
    patient_relation = rest_serializers.SerializerMethodField()
    status = rest_serializers.SerializerMethodField()

    def get_name(self, instance):
        return instance.portie.name

    def get_portie_phone_number(self, instance):
        return instance.portie.phone_number

    def get_patient_contact_number(self, instance):
        return instance.patient.phone_number

    def get_patient_relation(self, instance):
        return instance.patient_family.relation

    def get_status(self, instance):
        return instance.able_to_connect

    class Meta:
        model = patient_models.PortieCallingDetail
        fields = (
            "name",
            "portie_phone_number",
            "status",
            "patient_contact_number",
            "patient_relation",
            "status",
            "comments"
        )


class ContactDetailsSerializer(rest_serializers.ModelSerializer):
    contact_number_belongs_to = rest_serializers.SerializerMethodField()

    def get_contact_number_belongs_to(self, instance):
        return patient_models.PortieCallingDetail.objects.get(
            patient=instance).patient_family.relation if patient_models.PortieCallingDetail.objects.filter(
            patient=instance) else 'self'

    class Meta:
        model = patient_models.Patient
        fields = (
            "phone_number",
            "address",
            "district",
            "state",
            "contact_number_belongs_to",
            "local_body"
        )


class MedicationDetailsSerializer(rest_serializers.ModelSerializer):
    attendant_name = rest_serializers.SerializerMethodField()
    attendant_email = rest_serializers.SerializerMethodField()
    attendant_phone_number = rest_serializers.SerializerMethodField()

    def get_attendant_name(self, instance):
        return ''

    def get_attendant_email(self, instance):
        return ''

    def get_attendant_phone_number(self, instance):
        return ''

    class Meta:
        model = patient_models.Patient
        fields = (
            "symptoms",
            "diseases",
            "covid_status",
            "clinical_status",
            "attendant_name",
            "attendant_email",
            "attendant_phone_number",
        )


class PatientFacilityDetailsSerializer(rest_serializers.ModelSerializer):

    class Meta:
        model = facility_models.Facility
        fields = (
            "id",
            "name",
            "district",
            "facility_type",
            "owned_by"
        )


class PatientLabSerializer(rest_serializers.ModelSerializer):
    name = rest_serializers.SerializerMethodField()
    code = rest_serializers.SerializerMethodField()

    def get_name(self, instance):
        testing_lab = facility_models.TestingLab.objects.filter(id=instance.testing_lab.id)
        return testing_lab.first().name if testing_lab else ''

    def get_code(self, instance):
        testing_lab = facility_models.TestingLab.objects.filter(id=instance.testing_lab.id)
        return testing_lab.first().code if testing_lab else ''

    class Meta:
        model = patient_models.PatientSampleTest
        fields = (
            'name',
            'code',
            'date_of_sample',
            'result',
            'status_updated_at',
        )


class PersonalDetailsSerializer(rest_serializers.ModelSerializer):
    age_years = rest_serializers.IntegerField(source="year")
    age_months = rest_serializers.IntegerField(source="month")

    class Meta:
        model = patient_models.Patient
        fields = (
            "name", "icmr_id", "govt_id", "gender", "cluster_group", "age_years", "age_months",
        )


class PatientDetailsSerializer(rest_serializers.Serializer):
    personal_details = rest_serializers.SerializerMethodField()
    patient_family_details = rest_serializers.SerializerMethodField()
    portie_calling_details = rest_serializers.SerializerMethodField()
    contact_details = rest_serializers.SerializerMethodField()
    medication_details = rest_serializers.SerializerMethodField()
    patient_timeline = rest_serializers.SerializerMethodField()
    facility_details = rest_serializers.SerializerMethodField()
    patient_lab_details = rest_serializers.SerializerMethodField()

    def get_patient_family_details(self, instance):
        return PatientFamilySerializer(patient_models.PatientFamily.objects.filter(patient=instance), many=True).data

    def get_portie_calling_details(self, instance):
        return PortieCallingDetailSerializer(
            patient_models.PortieCallingDetail.objects.filter(patient=instance), many=True
        ).data

    def get_contact_details(self, instance):
        return ContactDetailsSerializer(patient_models.Patient.objects.filter(id=instance.id), many=True).data

    def get_medication_details(self, instance):
        return MedicationDetailsSerializer(patient_models.Patient.objects.filter(id=instance.id), many=True).data

    def get_facility_details(self, instance):
        return PatientFacilityDetailsSerializer(
            facility_models.Facility.objects.filter(id=instance.facility.id), many=True
        ).data

    def get_patient_timeline(self, instance):
        return PatientTimeLineSerializer(
            patient_models.PatientTimeLine.objects.filter(patient=instance), many=True
        ).data

    def get_patient_lab_details(self, instance):
        return PatientLabSerializer(patient_models.PatientSampleTest.objects.filter(patient=instance), many=True).data

    def get_personal_details(self, instance):
        print(instance)
        return PersonalDetailsSerializer(patient_models.Patient.objects.filter(id=instance.id), many=True).data

    class Meta:
        model = None
        fields = (
            "personal_details", "patient_family_details", "portie_calling_details", "contact_details",
            "medication_details",
            "facility_details", "patient_timeline", "patient_lab_details"
        )
