from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegisterSerializers
from django.contrib.auth.models import User
from django.conf import settings
import jwt

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserRegisterSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status =status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    '''
        request收到user name and password認證然後manual給jwt token
    '''
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        # object.get(username=username)get單一value 如果超過會exception
        if user is None:
            raise AuthenticationFailed("User not found")
        if not user.check_password(password):
            raise AuthenticationFailed("incorrect password")
        
        #jwt token自行設定 simeple-jwt傳輸資料過去

        refresh = RefreshToken.for_user(user)
        response = Response({'user':username, 'token':str(refresh.access_token)} ,
                            status=status.HTTP_200_OK)
        response.set_cookie(key= "jwt", value=refresh.access_token, httponly=True)
        return response


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response()
        response.delete_cookie('jwt') #key
        response.data = {
            'message': '成功登出'
        }
        return response



class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        #get到token payload
        authorization_header = request.META.get('HTTP_AUTHORIZATION')
        if authorization_header:
            # 提取出token值
            _, token = authorization_header.split(' ')
            JWT_SECRET_KEY = settings.SECRET_KEY
            decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
            user_id = decoded_token.get("user_id")
            #user從authmodel中找到useraname
            user = User.objects.get(id = user_id)
            serializer = UserRegisterSerializers(user)
            response = Response({'id':user_id,'info':serializer.data})
        return response


class DeleteAccountView(APIView):
    '''
    刪除帳戶delete orm操作 登陸狀態cookie中才能進行刪除(authenticated)
    
    post, (前端有登入才有delete button 所以會有cookie)
    後端登入cookie token反抓該用戶username比對然後做delete
    傳給serializer確認然後delete_user 
    '''
    permission_classes = [IsAuthenticated]
    def delete(self, request):

        #get info
        JWT_SECRET_KEY = settings.SECRET_KEY
        token = request.COOKIES.get('jwt')
        decoded_token = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        user_id = decoded_token.get("user_id")
        
        #orm delete
        user = User.objects.filter(id = user_id).first()
        user.delete()

        #response success or not
        response = Response()
        response.data = {
            "message":"刪除成功"
        }
        return response


{
    "username":"jjjj",
    "password":"klp264512"
}