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

    def validate(self, data):
        '''
            Custom Validators:
                - first_name: Required
                - last_name: Required
                - email: required
            All other fields are required by User model by default
        '''
        required_fields = ['first_name', 'last_name', 'email']

        # Iterate through required_fields list to check if each field is filled in
        for field in required_fields:

            # If field not filled, raise ValidationError
            if not data.get(field):
                raise serializers.ValidationError({field: f"{field.replace('_', ' ').capitalize()} is required."})
        
        return data


    # Checks for unique emails
    def validate_email(self, value):
        # If user, raise validation error
        if User.objects.filter(email=value).exists():
           raise serializers.ValidationError("This email address is already being used")
        # Return value if no errors
        return value
    
    # Creates new user
    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )

        # If successful, return user 
        return user
    

class LoginSerializer(serializers.ModelSerializer):
    '''
        Serializer for user login
    '''
    pass


