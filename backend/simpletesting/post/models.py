from django.db import models

# Create your models here.
class Post(models.Model):
    '''
    id=post location 作者 發布時間 內容 上傳圖片 擊掌數 內容區_id
    '''
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    picture = models.ImageField(blank=True)
    clap_count = models.IntegerField(default=0)
    

class Comment(models.Model):
    '''
    commentid userid postid content
    '''
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post_locate = models.ForeignKey(Post, related_name='commentat', on_delete=models.CASCADE,null=True)
    content = models.TextField()

