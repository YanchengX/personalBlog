from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    #這個instance一個model假設資料集不正確可以回傳邏輯到model orm在輸入至DB
    #create一個實例因為model作為abstract只作定義沒有instance所以從這邊
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            #from auth.model user
            instance.set_password(password)
        instance.save()
        return instance

#https://docs.djangoproject.com/en/4.2/ref/contrib/auth/#django.contrib.auth.models.User.set_password