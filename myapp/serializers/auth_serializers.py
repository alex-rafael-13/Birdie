from rest_framework import serializers
from django.contrib.auth.models import User #Using Django User Model


class RegisterSerializer(serializers.ModelSerializer):
    '''
        Serializer to register a new User
    '''
    
    #Make password write_only
    password = serializers.CharField(write_only=True)

    # Necessary fields for user creation
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'password', 'email']

    # Checks for unique emails
    def validate_email(self, value):
        # If user, raise validation error
        if User.objects.filter(email=value):
            serializers.ValidationError("This email address is already being used")
        # Return value if no errors
        return value
        
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
    


