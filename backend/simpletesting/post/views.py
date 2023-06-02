from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.http import Http404

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
'''
apiview funciton->
    from model operation
    post(all post)->get post put delete get comment
    comment get post delete 
'''

class PostList(APIView):
    '''
    get post and new a  post
    貼文show
    '''
    permission_classes = [AllowAny]
    def get(self, request, format = None):
        posty = Post.objects.all()
        serializer = PostSerializer(posty, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostOperation(APIView):
    '''
    update delete patch
    貼文操作
    '''
    permission_classes = [AllowAny]
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def delete(self, request, pk):
        postid = pk
        post = Post.objects.get(post_id=postid)
        post.delete()

        response = Response()
        response.data = {
            "message":"刪除成功"
        }
        return response

class CommentList(APIView):
    '''
    get -> commentid, userid, comment, post_locate
    post -> same request find userid, post_locate
    permission = allow any
    留言串
    '''
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many = True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CommentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentOperation(APIView):
    '''
    get post delete update -> isAuthenticated
    CRUD該留言
    '''
    permission_classes = [IsAuthenticated]
    
    def get_object(self,pk):
        try:
            return Comment.objects.get(pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request):
        comment = Comment.objects.all()
        comment.filter()
        serializer = CommentSerializer(comment)
        return Response(serializer.data)


class ClapCount(APIView):
    '''
    clap counthing from Post
    get
        文章選擇時選擇到的post對應他的id給serializer data 
        再丟入以下pk的位置對應文章url <int:pk> 進去找到該文章的clap數

    put
        點擊拍手進行增加計算， 

   '''
    permission_classes = [AllowAny]

    def get(self, request, pk, format=None):
        clap = Post.objects.all()
        serializer = PostSerializer(clap, many=True)
        clapcount = serializer.data[pk]['clap_count']
        return Response({"clap_count":clapcount})

    def put(self, request, pk):
        #pk 跟 id 差1
        post = Post.objects.get(pk=pk+1)
        post.clap_count += 1
        post.save()
        
        serializer = PostSerializer(post)
        return Response(serializer.data)

class PostCommentlist(APIView):
    '''
    合併查詢顯示貼文以及留言的API
    '''
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        postcomment = Post.objects.all()
        serializer = PostSerializer(postcomment, many=True)
        return Response(serializer.data)


{
    "username":"fuclyouall",
    "password":"abcd1234"
}
