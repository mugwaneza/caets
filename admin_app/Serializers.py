from django.contrib.gis import serializers
from django.http import HttpResponse
from admin_app.models import roles, department, members_personalinfo, guest_application, attendance
from rest_framework import serializers

class RolesSerializers(serializers.ModelSerializer):

    class Meta:
        model = roles
        fields = '__all__'

class DepartmentSerializers(serializers.ModelSerializer):

    class Meta:
        model = department
        fields = '__all__'

class MembersSerializer(serializers.ModelSerializer):

    role = RolesSerializers(read_only=True)
    dept = DepartmentSerializers(read_only=True)
    class Meta:
        model = members_personalinfo
        fields = '__all__'


class GuestApplicationSerializer(serializers.ModelSerializer):

    dept = DepartmentSerializers(read_only=True)
    class Meta:
        model = guest_application
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):

    member = MembersSerializer(read_only=True)
    guest = GuestApplicationSerializer(read_only=True)
    class Meta:
        model = attendance
        fields = '__all__'
