from rest_framework import serializers

from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.SerializerMethodField()
    selected = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = [
            'id',
            'created_by',
            'created_at',
            'question',
            'choices',
            'selected'
        ]

    def get_created_at(self, obj):
        return obj.created_at.strftime("%d/%m/%Y")

    def get_created_by(self, obj):
        return obj.created_by.username

    def get_selected(self, obj):
        exam = self.context['exam']
        selected_questions = list(exam.questions.values_list("pk", flat=True))
        return obj.pk in selected_questions

    def get_choices(self, obj):
        return obj.get_display_schema_choices
