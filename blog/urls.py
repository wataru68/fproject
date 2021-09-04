from django.urls import path
from django.urls.resolvers import URLPattern
from .import views

app_name = 'blog'

# URLパターンを登録するための変数
# リクエストされたURLのページへのフルパス部分が''(無し)にマッチングした場合
# viewモジュールのIndexViewクラスをインスタンス化する

urlpatterns = [
    # リクエストされたURLが""(無し)の場合
    # viewsモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),

    # リクエストされたURLが「blog-detail/レコードのid/」の場合は
    # BlogDetailを実行
    path(
        # 詳細ページのURLは「blog-detail/レコードのid/」
        'blog-datail/<int:pk>',
        # viewsモジュールのBlogDetailを実行
        views.BlogDetail.as_view(),
        # URLパターンの名前を'blog_detail'にする
        name='blog_detail'
    ),

    # scienceカテゴリの一覧ページのURLパターン
    path(
        'science-list/',
        views.ScienceView.as_view(),
        name='science_list'
    ),

    # dailylifeカテゴリの一覧ページのURLパターン
    path(
        'dailylife-list/',
        views.DailylifeView.as_view(),
        name='dailylife_list'
    ),

    # musicカテゴリの一覧ページのURLパターン
    path(
        'music-list/',
        views.MusicView.as_view(),
        name='music_list'
    ),

    # 問い合わせページのURLパターン
    path(
        # 問い合わせページのURLは「contact/」
        'contact/',
        # viewsモジュールのContactViewを実行
        views.ContactView.as_view(),
        # URLパターンの名前を'contact'にする
        name='contact',
    ),
]
