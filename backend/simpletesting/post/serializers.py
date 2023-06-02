from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    #commentset = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all())

    commentat = CommentSerializer(many = True,required=False) #comment 做foreign，做foreign的要在主model叫

    class Meta:
        model = Post
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    
    posts_user = PostSerializer(many = True)
    comment_user = CommentSerializer(many =True)

    class Meta:
        model = User
        fields = "__all__"

