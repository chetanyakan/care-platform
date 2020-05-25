from rest_framework import serializers as rest_serializer

from apps.facility import models as facility_models


class FacilitySerializer(rest_serializer.ModelSerializer):
    class Meta:
        model = facility_models.Facility
        fields = (
            "id",
            "name",
            "facility_code",
            "facility_type",
            "location",
            "address",
            "local_body",
            "district",
            "state",
            "phone_number",
            "corona_testing",
            "created_by",
            "owned_by",
            "total_patient",
            "positive_patient",
            "negative_patient",
        )


class FacilityUserSerializer(rest_serializer.ModelSerializer):
    class Meta:
        model = facility_models.FacilityUser
        fields = (
            "facility",
            "user",
            "created_by",
        )


class FacilityStaffSerializer(rest_serializer.ModelSerializer):
    class Meta:
        model = facility_models.FacilityStaff
        fields = (
            "id",
            "facility",
            "name",
            "phone_number",
            "email",
            "designation",
        )


class FacilityInfrastructureSerializer(rest_serializer.ModelSerializer):
    class Meta:
        model = facility_models.FacilityInfrastructure
        fields = (
            "id",
            "facility",
            "room_type",
            "bed_type",
            "total_bed",
            "occupied_bed",
            "available_bed",
            "created_by",
        )


class InventorySerializer(rest_serializer.ModelSerializer):
    class Meta:
        model = facility_models.Inventory
        fields = (
            "id",
            "facility",
            "item",
            "required_quantity",
            "current_quantity",
            "created_by",
        )
