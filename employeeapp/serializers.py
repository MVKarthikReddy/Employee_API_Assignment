from rest_framework import serializers
from employeeapp.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'name', 'dob', 'password', 'password2', 'tc']
        extra_kwargs = {
            "password" : {"write_only":True}
        }

    # validating password and confirm password while registration
    def validate(self,attrs):
        password = attrs.get('password')
        conpass = attrs.get('password2')
        if(password != conpass):
            raise serializers.ValidationError("password and Confirm Password doesn't match")
        return super().validate(attrs)

    def create(self,validate_data):
        return User.objects.create_user(**validate_data)

    

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ["email", "password"]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "name","dob"]

        
