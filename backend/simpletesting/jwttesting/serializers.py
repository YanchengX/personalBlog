from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
        #不顯示password
        extra_kwargs = {
            "password":{'write_only' : True}
        }
    
    #overwrite create method
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data.get('email'),
            password  = validated_data['password']
        )  
        return user
    
class DeleteAccountSerializers(serializers.ModelSerializer):
    pass

