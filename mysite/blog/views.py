# Views.pyは関数とHTMLファイルを紐付けする。
from django.http import Http404
from django.shortcuts import get_object_or_404,render
# renderメソッドを使用するために、インポート
# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
# djangoのhttpモジュールから、HttpResponseクラスをimport

from django.urls import reverse

from django.template import loader
# テンプレートの読み込み

from django.views import generic

from .models import Question,Choice
# Questionオブジェクトの読み込み

from django.shortcuts import render




class IndexView(generic.ListView):
    template_name = 'blog/Work.html'
    context_object_name='latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

"""class DetailView(generic.DetailView):
    model = Question
    template_name = 'blog/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'blog/results.html'"""


# def index(request):


    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # order_byはメソッド
    # Model.objects.order_by('記事')
    # Questionをorder_by(-pub_date)でソートし、前から５つの配列を取得
    # マイナスをつけるだけでデータを降順にしてくれる。
    # [:5]は配列をスライスする。[0:5]と同じで０番目から５つを取得する。

    # template = loader.get_template('blog/index.html')
    # テンプレートの読み込み
    # loader.get_templatesで（）内の指定ファイル読み込み

    # context = {
      #   'latest_question_list': latest_question_list,
    # }
    
    # {}ディクショナリ型、テンプレートで使う変数を設定、{キー：値、キー：値、}

    # return render(request,'polls/index.html',context)
    # return render(request,template_name,context=None,context_type=None,status=None,using=None)
    # template_nameには相対パスで指定する。
    # contextには辞書型のデータを指定する。
    # HttpResponseをrenderで置き換え
    # renderメソッド、指定されたテンプレートをレンダリングしてHttpResponseを返すためのメソッド



    # return HttpResponse("Hello,world.You're at the blog index.")

    # HttpResponseは()内の文字をブラウザに表示させる？○○？←文法不明

# def detail(request,question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    # "You're looking at question {}.".format(question_id)を古い記述方式
    # try:
        # question=Question.objects.get(pk=question_id)
        # 主キーはそのカラム名に関わらずpk=で検索できる。
    # except Question.DoesNotExist:
        # raise Http404("Question does not exist")

    # return render(request,'polls/detail.html',{'question':question})
  #   question = get_object_or_404(Question,pk=question_id)
    #Questionモデルからpk=question_idのものが返され、question変数に格納、存在しない際はHttp404となる。
    # get_object_or_404はdjango.shortcutsに用意されているショートカット関数。
    # get_object_or_404(モデル名 , pk)
    # ここではQuestionモデルからpk=question_ideのレコードをquestion変数に代入している。
    # return render(request,'blog/detail.html',{'question':question})

# def results(request, question_id):
    # response = "You're lokking at the results of question %s."
    # Responseを一回定数にいれている。上記のdetailと同じ
    # question = get_object_or_404(Question,pk=question_id)
    # return HttpResponse(response % question_id)
   #  return render(request,'polls/results.html',{'question':question})

"""def vote(request,question_id):
    #return HttpResponse("You're voting on question %s." % question_id)

    question = get_object_or_404(Question,pk=question_id)
    # get_object_or_404はdjango.shortcutsに用意されているショートカット関数。
    # get_object_or_404(モデル名 , pk)
    # ここではQuestionモデルからpk=question_idのレコードをquestion変数に代入している。
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # Questionテーブルが外部参照しているChoiceテーブルのデータ、という意味
        # (テーブル1).(テーブル2)_setのようなイメージ
        # choice_setはquestionオブジェクトに対してリレーションを張っているchoiceモデルを操作するためのmanager
        # テーブル1に定義されている外部キーに紐付いているテーブル2のような関係
        # postされた値は、request.POSTに辞書の様な形式で入っている。
        # inoutタグのname属性値がchoiceなのでrequest.POST['choice]で選択肢が取れる。
        # 変数selected_choice にquestionオブジェクトに対してget関数で取得した条件があうオブジェクト変数を代入

    except (KeyError, Choice.DoesNotExist):
        # try,exceptの構文
        # exceptに複数の例外クラスを設定する。
        # keyerror,DoesNotExistが発生した時にエラーを受け取ることができる。
        # KeyError :辞書等のキーエラー
        # モデルクラス.objects.get(条件)といった形でクエリを発行した場合、ヒットしなかった場合はモデルクラス.DoesNotExistという例外が発生する。
        return render(request,'blog/detail.html',{
            'question':question,
            'error_message':"You didn't selecte a choice.",
        })
        # renderメソッドは、指定されたテンプレートをレンダリングして、HttpResponseを返すためのメソッド。
        # レンダリングとは、形を変えて表現すること（例：ブラウザはhtmlを人が読み取れる様に変えて表現）
        # render()は「結果をウェブページに表示」する機能
        # render(request, template ,context)
        # 第一引数で「requestオブジェクト」受け取り。第二引数で「表示するhtml」を指定、第三引数で「テンプレートに渡す変数」を指定する。

    else:
        selected_choice.votes += 1
        # ???
        selected_choice.save()
        # formから受け取った値を保存する。
        return HttpResponseRedirect(reverse('blog:results',args=(question.id,)))
        # HttpResponseRedirectとreverseとの組み合わせ
        # blogというアプリのresultというviewへの遷移先を記述
        # args(アーグス)へはtoupleで渡す必要があるため、()で囲み且つ閉じ()前にカンマを記述。args:可変長引数
        # redirect関数は、表示画面を遷移させる際に使用
        # HttpResponseRedirect('URL')でURLにリダイレクトされる。
        # reverse関数を用いると、関数名からURLを逆引きできる。reverseはページ名からURLを取得するメソッド
        # reverse(viewname,urlconf=None,args=None,kwargs=None,current_app=None)
        # viewnameはurlpatternsで名前づけされているURLの名前
        # 今回の'blog:result'は'アプリ名：URLname'で指定されている。

def test(request):
    template_name="blog/test.html"
    return render(request,template_name)"""

