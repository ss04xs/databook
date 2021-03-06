import json
from collections import OrderedDict
from django.http import HttpResponse
from cms.models import DataBook, Chant


def render_json_response(request, data, status=None):
    """response を JSON で返却"""
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')  # POSTでJSONPの場合
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
    return response


def databook_list(request):
    """選手データと感想のJSONを返す"""
    databooks = []
    for databook in DataBook.objects.all().order_by('id'):

        comments = []
        for comment in databook.comments.order_by('id'):
            comment_dict = OrderedDict([
                ('id', comment.id),
                ('comment', comment.comment),
            ])
            comments.append(comment_dict)
        databook_dict = OrderedDict([
            ('id', databook.id),
            ('name', databook.name),
            ('club', databook.club),
            ('num', databook.num),
            ('position', databook.position),
            ('height', databook.height),
            ('weight', databook.weight),
            ('foot_handed', databook.foot_handed),
            ('previous_team', databook.previous_team),
            ('image_url', databook.image_url),
            ('comments', comments)
        ])
        databooks.append(databook_dict)

    data = OrderedDict([ ('databooks', databooks) ])
    return render_json_response(request, data)

def chant_list(request):
    """選手データと感想のJSONを返す"""
    chants = []
    for chant in Chant.objects.all().order_by('id'):

        chant_dict = OrderedDict([
            ('タイトル', chant.title),
            ('歌詞', chant.chant)
        ])
        chants.append(chant_dict)

    data = OrderedDict([ ('chants', chants) ])
    return render_json_response(request, data)