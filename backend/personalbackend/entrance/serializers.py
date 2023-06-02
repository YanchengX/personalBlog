from rest_framework import serializers
from .models import Login, Signup, Identify, Information

class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Signup
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'

class IdentifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Identify
        fields = '__all__'

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'