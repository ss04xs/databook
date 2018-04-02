# Generated by Django 2.0.3 on 2018-04-01 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, verbose_name='コメント')),
            ],
        ),
        migrations.CreateModel(
            name='DataBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='選手名')),
                ('club', models.CharField(blank=True, max_length=255, verbose_name='所属クラブ')),
                ('num', models.IntegerField(blank=True, default=0, verbose_name='背番号')),
                ('position', models.CharField(blank=True, max_length=255, verbose_name='ポジション')),
                ('height', models.IntegerField(blank=True, default=0, verbose_name='身長')),
                ('weight', models.IntegerField(blank=True, default=0, verbose_name='体重')),
                ('foot_handed', models.CharField(blank=True, max_length=255, verbose_name='利き足')),
                ('previous_team', models.CharField(blank=True, max_length=255, verbose_name='前所属クラブ')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='databook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='cms.DataBook', verbose_name='選手名'),
        ),
    ]
