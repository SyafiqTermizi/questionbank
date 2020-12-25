from django.db.models import fields
from rest_framework import serializers

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.SerializerMethodField()
    class Meta:
        model = Question
        fields = '__all__'

    def get_choices(self, obj):
        return obj.get_display_schema_choices
