from rest_framework import serializers

from bug.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class BugsSerializer(serializers.Serializer):
    id = serializers.IntegerField()

    description = serializers.CharField(max_length=100)
    # username = serializers.StringRelatedField(source='user')
    username = serializers.SlugRelatedField(
        source="user", slug_field="username", read_only=True
    )
    project = serializers.SlugRelatedField(slug_field="name", read_only=True)
