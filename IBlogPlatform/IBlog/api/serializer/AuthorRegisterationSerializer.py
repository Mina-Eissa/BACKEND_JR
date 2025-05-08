
from rest_framework import serializers
from ..models import Author
from django.contrib.auth.hashers import make_password


class AuthorRegisterationSerializer(serializers.ModelSerializer):
    authPassword = serializers.CharField(write_only=True)

    class Meta:
        model = Author
        fields = [
            'id',
            'authName',
            'authEmail',
            'authImg',
            'authWallpaper',
            'authBirthDate',
            'authBio',
            'authCreatedAt',
            'authUpdatedAt',
            'authPassword',
        ]
        read_only_fields = ['id', 'authCreatedAt', 'authUpdatedAt']

    def create(self, validated_data):
        # Hash the password before saving
        validated_data['authPassword'] = make_password(
            validated_data['authPassword'])
        author = Author.objects.create(**validated_data)
        return author
