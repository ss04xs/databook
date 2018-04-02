from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # 選手データ
    path('databook/', views.databook_list, name='databook_list'),   # 一覧
    path('databook/add/', views.databook_edit, name='databook_add'),  # 登録
    path('databook/mod/<int:databook_id>/', views.databook_edit, name='databook_mod'),  # 修正
    path('databook/del/<int:databook_id>/', views.databook_del, name='databook_del'),   # 削除
    # コメント
    path('comment/<int:databook_id>/', views.CommentList.as_view(), name='comment_list'),  # 一覧
    path('comment/add/<int:databook_id>/', views.comment_edit, name='comment_add'),        # 登録
    path('comment/mod/<int:databook_id>/<int:comment_id>/', views.comment_edit, name='comment_mod'),  # 修正
    path('comment/del/<int:databook_id>/<int:comment_id>/', views.comment_del, name='comment_del'),   # 削除
]