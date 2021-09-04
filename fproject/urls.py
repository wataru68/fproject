# ルーティングを記述するためのモジュール、URLconf(URL設定)を定義
from django.contrib import admin
from django.urls import path, include  # includeを追加
# 第一引数に対応するurlへのリクエストが来た場合に
# 第二引数に対応するviewsを呼び出す
urlpatterns = [
    # リクエストされたURLのフルパス部分がadmin/にマッチングした場合
    # admin.site.urlsを呼び出し、Django管理サイトを表示
    path('admin/', admin.site.urls),

    # http(s)://<ホスト名>/以下のURLパターンにblogアプリの
    # URLconf(urls.py)を含める
    path('', include('blog.urls')),
]
