from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tweet/create/', views.create_tweet, name='create_tweet'),
    path('tweet/', views.show_tweet, name='show_tweet'),
    path('tweet/detail/<int:detail_id>', views.detail_tweet, name='detail'),
    path('tweet/update/<int:update_id>', views.update_tweet, name='update'),
    path('tweet/delete/<int:delete_id>', views.delete_tweet, name='delete'),
    path('tweet/mypage/<int:user_id>', views.my_page, name='my_page'),
    path('tweet/likes/<int:tweet_id>', views.like_create, name='like_create')
]


# 댓글보이기
# 'tweet/detatil/{tweet_id} 상세페이지에 댓글보여주기? or 메인페이지에 tweet에 하단에 댓글을 만들지 고민! 만약 하단에 만들면 줄여주는 하이퍼링크같은게 있어야 함
# 댓글 작성
# 'tweet/댓글을 메인에서 보여주고 만들게 해야할지 아니면 작성해놓은 상세페이지에 보여주는지 고민
# 댓글 삭제
# 'tweet/delete' 댓글 삭제하기
