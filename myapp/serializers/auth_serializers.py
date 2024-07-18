from rest_framework import serializers
from django.contrib.auth.models import User #Using Django User Model

class RegisterSerializer(serializers.ModelSerializer):
    '''
        Serializer to register a new User
    '''

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'password', 'email']

    # Creates new user
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["first_name"],
            username=validated_data["last_name"],
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )

        # If successful, return user 
        return user


