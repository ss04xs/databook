from django.db import models


class DataBook(models.Model):
    """選手データ"""
    name = models.CharField('選手名', max_length=255)
    club = models.CharField('所属クラブ', max_length=255, blank=True)
    num = models.IntegerField('背番号', blank=True, default=0)
    position = models.CharField('ポジション', max_length=255, blank=True)
    height = models.IntegerField('身長', blank=True, default=0)
    weight = models.IntegerField('体重', blank=True, default=0)
    foot_handed = models.CharField('利き足', max_length=255, blank=True)
    previous_team = models.CharField('前所属クラブ', max_length=255, blank=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    """感想"""
    databook = models.ForeignKey(DataBook, verbose_name='選手名', related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment