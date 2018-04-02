from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.http import HttpResponse

from cms.models import DataBook, Comment
from cms.forms import DataBookForm, CommentForm


def databook_list(request):
    """選手データの一覧"""
#    return HttpResponse('選手データの一覧')
    databooks = DataBook.objects.all().order_by('num')
    return render(request,
                  'cms/databook_list.html',     # 使用するテンプレート
                  {'databooks': databooks})         # テンプレートに渡すデータ


def databook_edit(request, databook_id=None):
    """選手データの編集"""
#     return HttpResponse('選手データの編集')
    if databook_id:   # book_id が指定されている (修正時)
        databook = get_object_or_404(DataBook, pk=databook_id)
    else:         # book_id が指定されていない (追加時)
        databook = DataBook()

    if request.method == 'POST':
        form = DataBookForm(request.POST, instance=databook)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            databook = form.save(commit=False)
            databook.save()
            return redirect('cms:databook_list')
    else:    # GET の時
        form = DataBookForm(instance=databook)  # book インスタンスからフォームを作成

    return render(request, 'cms/databook_edit.html', dict(form=form, databook_id=databook_id))


def databook_del(request, databook_id):
    """選手データの削除"""
#     return HttpResponse('選手データの削除')
    databook = get_object_or_404(DataBook, pk=databook_id)
    databook.delete()
    return redirect('cms:databook_list')


class CommentList(ListView):
    """感想の一覧"""
    context_object_name='comments'
    template_name='cms/comment_list.html'
    paginate_by = 2  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        databook = get_object_or_404(DataBook, pk=kwargs['databook_id'])  # 親の選手データを読む
        comments = databook.comments.all().order_by('id')   # 選手データの子供の、感想を読む
        self.object_list = comments

        context = self.get_context_data(object_list=self.object_list, databook=databook)    
        return self.render_to_response(context)

def comment_edit(request, databook_id, comment_id=None):
    """感想の編集"""
    databook = get_object_or_404(DataBook, pk=databook_id)  # 親の選手データを読む
    if comment_id:   # comment_id が指定されている (修正時)
        comment = get_object_or_404(Comment, pk=comment_id)
    else:               # comment_id が指定されていない (追加時)
        comment = Comment()

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            comment = form.save(commit=False)
            comment.databook = databook  # この感想の、親の選手データをセット
            comment.save()
            return redirect('cms:comment_list', databook_id=databook_id)
    else:    # GET の時
        form = CommentForm(instance=comment)  # comment インスタンスからフォームを作成

    return render(request,
                  'cms/comment_edit.html',
                  dict(form=form, databook_id=databook_id, comment_id=comment_id))


def comment_del(request, databook_id, comment_id):
    """感想の削除"""
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('cms:comment_list', databook_id=databook_id)