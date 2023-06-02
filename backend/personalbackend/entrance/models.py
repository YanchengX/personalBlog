from django.db import models

#註冊
class Signup(models.Model):
    account =  models.CharField(max_length=100)
    pwd = models.CharField(max_length=300)
    
#個人資料
class Information(models.Model):
    signupinfo = models.ForeignKey(Signup, on_delete=models.CASCADE, default=1)
    username = models.CharField(max_length=100)

#登入
class Login(models.Model):
    signupinfo = models.ForeignKey(Signup, on_delete=models.CASCADE, default=1)
    login_at = models.DateTimeField(auto_now_add=True)

#身分別
class Identify(models.Model):
    signupinfo = models.ForeignKey(Signup, on_delete=models.CASCADE, default=1)
    identify = models.BooleanField()
