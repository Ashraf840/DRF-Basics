from rest_framework import serializers
from .models import User
from rest_framework.validators import ValidationError


class UserSignupSerializer(serializers.ModelSerializer):

    # Adding attributes of this class only add some extra validations, in "ModelSerializer", it's not determied in this section how many attributes can be passed while making a POST request.
    email=serializers.CharField(max_length=80)
    username=serializers.CharField(max_length=45)
    password=serializers.CharField(min_length=8, write_only=True)   # Hide the password while sending response to client end

    class Meta:
        model=User
        # It's determined here, how many attributes will be passed while making the POST request & what there names will be.
        fields=['email', 'username', 'data_of_birth', 'password']

    def validate(self, attrs):
        # Check if email exist in the system
        if User.objects.filter(email=attrs.get('email')).exists():
            raise ValidationError("Email is already taken!")
        return super().validate(attrs)
    
    def create(self, validated_data):
        password=validated_data.pop('password') # Pops out the password
        user=super().create(validated_data) # Create user using this "create()" method
        user.set_password(password)
        user.save()
        return user