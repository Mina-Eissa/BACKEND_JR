from rest_framework import serializers
from ..models import Author


class AuthorLoggingInSerializer(serializers.ModelSerializer):
    authPassword = serializers.CharField(write_only=True)

    class Meta:
        model = Author
        fields = [
            'authName',
            'authEmail',
            'authPassword',
        ]
    def validate(self, attrs):
        auth_name = attrs.get('authName')
        auth_email = attrs.get('authEmail')

        if not auth_name and not auth_email:
            raise serializers.ValidationError("Either 'authName' or 'authEmail' must be provided.")
        
        # if auth_name and auth_email:
        #     raise serializers.ValidationError("Please provide either 'authName' or 'authEmail', not both.")

        return attrs