from django.urls import path
from api import views

app_name = 'api'
urlpatterns = [
    # 選手データ
    path('v1/databooks/', views.databook_list, name='databook_list'),   # 一覧
]