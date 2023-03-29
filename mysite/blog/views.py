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
    template_name = "blog/Work.html"
    context_object_name='latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


"""def top_page(request):
    template_name="Work.html"
    return render(request,template_name)"""

def trivia_greatman(request):
    template_name="blog/trivia_greatman.html"
    return render(request,template_name)

def life_summary(request):
    template_name="blog/life_summary.html"
    return render(request,template_name)

def trivia_summary(request):
    template_name="blog/trivia_summary.html"
    return render(request,template_name)

def trivia_rich(request):
    template_name="blog/trivia_rich.html"
    return render(request,template_name)

def trivia_athlete_rich(request):
    template_name="blog/trivia_athlete_rich.html"
    return render(request,template_name)

def trivia_artist_rich(request):
    template_name="blog/trivia_comedian.html"
    return render(request,template_name)

def trivia_athlete_rich(request):
    template_name="blog/trivia_athlete_rich.html"
    return render(request,template_name)

def trivia_soccer_goal(request):
    template_name="blog/trivia_soccer_goal.html"
    return render(request,template_name)

def trivia_comedian(request):
    template_name="blog/trivia_comedian.html"
    return render(request,template_name)

def trivia_game(request):
    template_name="blog/trivia_game.html"
    return render(request,template_name)

def trivia_baseball_homerun(request):
    template_name="blog/trivia_baseball_homerun.html"
    return render(request,template_name)

def trivia_potatochips(request):
    template_name="blog/trivia_potatochips.html"
    return render(request,template_name)

def trivia_population(request):
    template_name="blog/trivia_population.html"
    return render(request,template_name)

def trivia_game2(request):
    template_name="blog/trivia_game.html"
    return render(request,template_name)

def diary_230110(request):
    template_name="blog/diary_230110.html"
    return render(request,template_name)

def diary_summary(request):
    template_name="blog/diary_summary.html"
    return render(request,template_name)

def diary_230114(request):
    template_name="blog/diary_230114.html"
    return render(request,template_name)

def diary_230115(request):
    template_name="blog/diary_230115.html"
    return render(request,template_name)

def humor_summary(request):
    template_name="blog/humor_summary.html"
    return render(request,template_name)

def humor_seiza(request):
    template_name="blog/humor_seiza.html"
    return render(request,template_name)

def humor_busaiku(request):
    template_name="blog/humor_busaiku.html"
    return render(request,template_name)

def humor_ladytalk(request):
    template_name="blog/humor_ladytalk.html"
    return render(request,template_name)

def humor_party(request):
    template_name="blog/humor_party.html"
    return render(request,template_name)

def humor_smart(request):
    template_name="blog/humor_smart.html"
    return render(request,template_name)

def humor_macchan(request):
    template_name="blog/humor_macchan.html"
    return render(request,template_name)

def humor_propose(request):
    template_name="blog/humor_propose.html"
    return render(request,template_name)

def humor_nickname(request):
    template_name="blog/humor_nickname.html"
    return render(request,template_name)

def humor_yourself(request):
    template_name="blog/humor_yourself.html"
    return render(request,template_name)

def humor_positive(request):
    template_name="blog/humor_positive.html"
    return render(request,template_name)

def humor_life(request):
    template_name="blog/life_fx.html"
    return render(request,template_name)

def humor_soccer_tsukkomi(request):
    template_name="blog/humor_soccer_tsukkomi.html"
    return render(request,template_name)

def humor_baseball_tsukkomi(request):
    template_name="blog/humor_baseball_tsukkomi.html"
    return render(request,template_name)




def life_fx(request):
    template_name="blog/life_fx.html"
    return render(request,template_name)

def life_kabu(request):
    template_name="blog/life_kabu.html"
    return render(request,template_name)

def life_coin(request):
    template_name="blog/life_coin.html"
    return render(request,template_name)