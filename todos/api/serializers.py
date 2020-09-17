from rest_framework import serializers
from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        exclude = [
            "author",
            "updated_at",
        ]


    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")
