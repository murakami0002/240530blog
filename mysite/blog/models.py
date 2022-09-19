from django.db import models

import datetime
# Create your models here.
from django.db import models
#django.dbのmodelsファイルをimport
from django.utils import timezone

# テーブルは表のこと、カラムは列のこと、レコードは行のこと、フィールドは格納されている値のこと
class Question(models.Model):
    #各モデルは１つのクラスで表現されていて、いずれもdjango.db.models.Modelのサブクラス
    question_text = models.CharField(max_length=200)
    #インスタンス生成、変数名＝クラス名（引数）
     #各フィールドはFieldクラスのインスタンスとして表現
    #文字のフィールドで各フィールドにどのようなデータ型を保存するか記憶させる
    pub_date = models.DateTimeField('date published')
    #Djangoのモデルに日付と時刻を記録させる。
    #日時のフィールドでどのようなデータ型をDjangoに記憶させる。
    #question_text,pub_dateは機械可読なフィールド名,pub_dateには人間可読なフィールド名も指定
    def __str__(self):
        return self.question_text
    #インスタンスの表示を文字列で返す（シェルを使用した場合）
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #リレーションフィールド：ForeignKey,OneToOneField,ManyToManyFieldが存在
    #「多対一」の関係を持つ２つの異なるモデルを結び付けるため、ForeignKeyを使用
    #(to,on_detele)の２つの引数を必ず指定する必要あり。
    #toには紐付けるモデルを指定し、on_deleteには親フィールドが削除された際の動作
    #「1」になるモデルが親、「多」になるモデルが子。ForeignKeyのフィールドは子側に作成
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #整数を保存するためのフィールド、-2147483648~2147483647を格納するために使用。
    #default=0は初期値０を示す。何も入力なければ０が入っている。
    def __str__(self):
        return self.choice_text

class Post(models.Model):
  image = models.ImageField(upload_to="uploads/", null=True, blank=True)
