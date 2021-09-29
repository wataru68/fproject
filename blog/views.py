from django.shortcuts import render
# django.views.genericからListView, DetailViewをインポート
from django.views.generic import ListView, DetailView
# モデルBlogPostをインポート
from .models import BlogPost
# django.views.genericからFormViewをインポート
from django.views.generic import FormView
# django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy
# formsモジュールからContactFormをインポート
from .forms import ContactForm
# django.contribからmessagesをインポート
from django.contrib import messages


class IndexView(ListView):
    '''トップページのビュー

    投稿記事を一覧表示するのでListViewを継承

    Attributes(属性):
      template_name: レンダリングするテンプレート
      context_object_name: object_listキーの別名を設定
      queryset: データベースのクエリ
    '''
    # index.htmlをレンダリングする
    template_name = 'index.html'
    # object_listキーの別名を設定
    context_object_name = 'orderby_records'
    # モデルBlogPostのオブジェクトにorder_by()を適用して
    # BlogPostのレコードを投稿日時の降順で並び替える
    queryset = BlogPost.objects.order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 4


class BlogDetail(DetailView):
    '''詳細ページのビュー

    投稿記事の詳細を表示するのでDetailViewを継承する
    Attribute:
        template_name: レンダリングするテンプレート
        Model: モデルのクラス
    '''
    # post.htmlをレンダリングする
    template_name = 'post.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost


class HobbyView(ListView):
    '''趣味(hobby)カテゴリの記事を一覧表示するビュー'''
    # hobby_list.htmlをレンダリングする
    template_name = 'hobby_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'hobby_records'
    # category = 'hobby'のレコードを抽出して投稿日時の降順で並び替える
    queryset = BlogPost.objects.filter(
        category='hobby').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 2


class DailylifeView(ListView):
    '''日常(dailylife)カテゴリの記事を一覧表示するビュー'''
    # dailylife_list.htmlをレンダリングする
    template_name = 'dailylife_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'dailylife_records'
    # category = 'dailylife'のレコードを抽出して投稿日時の降順で並び替える
    queryset = BlogPost.objects.filter(
        category='dailylife').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 2


class KnowledgeView(ListView):
    '''知識(knowledge)カテゴリの記事を一覧表示するビュー'''
    # knowledge_list.htmlをレンダリングする
    template_name = 'knowledge_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'knowledge_records'
    # category = 'knowledge'のレコードを抽出して投稿日時の降順で並び替える
    queryset = BlogPost.objects.filter(
        category='knowledge').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 2


class ContactView(FormView):
    '''問い合わせページを一覧表示するビュー

    '''
    # contact.htmlをレンダリングする
    template_name = 'contact.html'
    # クラス変数 form_classにform.pyで定義したContactFormを設定
    form_class = ContactForm
    # 送信完了後にリダイレクトするページ
    success_url = reverse_lazy('blog:contact')

    def form_valid(self, form):
        '''FormViewクラスのform_valid()をオーバーライド
           フォームのバリデーションを通過したデータがPOSTされたときに呼ばれる
           メール送信を行う

           parameters:
             form(django.forms.Form):
               form_classに格納されているフォームのオブジェクト
           Return:
             HttpResponseRedirectのオブジェクト
             オブジェクトをインスタンス化するとsuccess_urlで
             設定されているURLにリダイレクトされる
        '''
        # form.pyのsend_email()を実行してメール送信を行う
        form.send_email()
        # 送信完了後に表示するメッセージ
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。')
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)
