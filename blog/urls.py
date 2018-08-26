from django.urls import path
from . import views

urlpatterns = [
    # ルートURLにアクセスした場合、ビューとしてviews.post_listを返す。
    path('', views.post_list, name='post_list'),
    # post/newにアクセスした場合、 views.post_newを返す。
    path('post/new', views.post_new, name='post_new'),
    # drafts/にアクセスした場合、 views.post_draft_listを返す。
    path('drafts/', views.post_draft_list, name='post_draft_list'),

    # post/の後に整数の値が指定されることを期待している。（pk変数に値を設定される）
    # post/pk/にアクセスした場合、views.post_detailを返す。（リスト面のタイトルで使用）
    path('post/<int:pk>/', views.post_detail, name='post_detail'), 
    # post/pk/edit/にアクセスした場合、views.post_editを返す。（詳細画面の編集ボタンで使用）
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # post/pk/publish/にアクセスした場合、views.post_publishを返す。（詳細画面のPublishボタンで使用）
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    # post/pk/remove/にアクセスした場合、views.post_removeを返す。（詳細画面の削除ボタンで使用）
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    
    # post/pk/comment/にアクセスした場合、views.add_comment_to_postを返す。（詳細画面のadd_commentボタンで使用）
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    # post/pk/approve/にアクセスした場合、views.comment_approveを返す。（詳細画面のコメント承認ボタンで使用）
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    # post/pk/remove/にアクセスした場合、views.comment_removeを返す。（詳細画面のコメント削除ボタンで使用）
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]

