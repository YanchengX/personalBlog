from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime


# Create your views here.
class RegisterView(APIView):
    #save是model的方法從create中instance這個變數他代表model然後作回回覆，siralizers為modelserialize所以create會自動呼叫。
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    #設定post請求
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        #篩選 orm object查詢
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        #check_password from auth.model user
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        #jwt 設定 header, payload, VERIFY SIGNATURE
        payload = {
            #3字母以內
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        #製作cookie session
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response

    #只要在view中提中rest相關字就可以接受然後再postman跟localhost會看到允許delete出現，
    def patch(self, request):
        pass

class UserView(APIView):

    #登入介面看cookie誰在登入中，
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):

    #post 實例一個response刪除cookie就完成
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success to logout'
        }
        return response


