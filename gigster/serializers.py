from rest_framework import serializers
from .models import Gig, Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class GigSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = Gig
        fields = ('id', 'title', 'slug', 'description', 'company', 'role', 'created_by')
        read_only_fields = ['created_at']