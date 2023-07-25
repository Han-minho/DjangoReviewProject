from django.urls import path, re_path
from blog import views
from blog.feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    # post views
    path('list/', views.post_list, name='post_list'),
    path('', views.PostListview.as_view(), name='post_list'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2})/(?P<post>[-\w]+)/$',
            views.post_detail, name='post_detail'),
    # path('<int:id>/', views.post_detail, name='post_detail'),
    # path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]