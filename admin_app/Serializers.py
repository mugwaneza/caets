from django.contrib.gis import serializers
from django.http import HttpResponse
from admin_app.models import roles, department, members_personalinfo, guest_application, attendance
from rest_framework import serializers
from index_app.models import visitor_chat, visitor_chat_message


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

class VisitorChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = visitor_chat
        fields = '__all__'


class VisitorChatMessageSerializer(serializers.ModelSerializer):

    posted_by_id = VisitorChatSerializer(read_only=True)
    class Meta:
        model = visitor_chat_message
        fields = '__all__'

