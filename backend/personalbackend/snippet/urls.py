from django.urls import path, include
from .views import SnippetViewSet, UserViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippet', SnippetViewSet,basename="snippet")
router.register(r'users', UserViewSet,basename="user")

urlpatterns = [
    path('', include(router.urls)),
]


# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = [
#     path('', api_root),
#     path('snippet/', snippet_list, name='snippet-list'),
#     path('snippet/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippet/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ]


# --------------------


# urlpatterns = [
#     path('', views.api_root),
#     path('snippet/', views.SnippetList.as_view(), name='snippet-list'),
#     path('snippet/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),

#     path('users/', views.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
# ]

#urlpatterns = format_suffix_patterns(urlpatterns)

#the api-auth actually canwhateveer URL i want to use is self-definition
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]