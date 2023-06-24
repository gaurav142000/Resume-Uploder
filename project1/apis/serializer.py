from rest_framework import serializers
from app1.models import *

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resume
        fields='__all__'
