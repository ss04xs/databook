from django.forms import ModelForm
from cms.models import DataBook, Comment


class DataBookForm(ModelForm):
    """選手データのフォーム"""
    class Meta:
        model = DataBook
        fields = ('name', 'club', 'num', 'position', 'height', 'weight', 'foot_handed', 'previous_team', 'image_url')

class CommentForm(ModelForm):
    """感想のフォーム"""
    class Meta:
        model = Comment
        fields = ('comment', )