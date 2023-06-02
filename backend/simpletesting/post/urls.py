from django.urls import path 
from .views import PostList, CommentList, ClapCount, PostCommentlist, PostOperation, CommentOperation

urlpatterns = [     
    path('postlist', PostList.as_view(), name='postlist'), 
    path('commentlist', CommentList.as_view(), name='commentlist'), 
    path('clapcount/<int:pk>', ClapCount.as_view(), name='clapcount'),
    path('postcommentlist', PostCommentlist.as_view(), name='postcommentlist'),
    path('postoperation/<int:pk>', PostOperation.as_view(), name='postoperation'), 
    path('commentoperation/<int:pk>', CommentOperation.as_view(), name='commentoperation'), 
    ]
