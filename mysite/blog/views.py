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

def trivia_break(request):
    template_name="blog/trivia_break.html"
    return render(request,template_name)

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

def humor_fart(request):
    template_name="blog/humor_fart.html"
    return render(request,template_name)

def humor_nosehair(request):
    template_name="blog/humor_nosehair.html"
    return render(request,template_name)

def humor_badbreath(request):
    template_name="blog/humor_badbreath.html"
    return render(request,template_name)

def humor_bodyodor(request):
    template_name="blog/humor_bodyodor.html"
    return render(request,template_name)

def humor_footodor(request):
    template_name="blog/humor_footodor.html"
    return render(request,template_name)

def humor_booger(request):
    template_name="blog/humor_booger.html"
    return render(request,template_name)

def humor_silent(request):
    template_name="blog/humor_silent.html"
    return render(request,template_name)

def humor_boss(request):
    template_name="blog/humor_boss.html"
    return render(request,template_name)

def humor_junior(request):
    template_name="blog/humor_junior.html"
    return render(request,template_name)

def humor_reunion(request):
    template_name="blog/humor_reunion.html"
    return render(request,template_name)

def humor_makeup(request):
    template_name="blog/humor_makeup.html"
    return render(request,template_name)

def humor_parent(request):
    template_name="blog/humor_parent.html"
    return render(request,template_name)

def humor_friends(request):
    template_name="blog/humor_friends.html"
    return render(request,template_name)

def humor_toilet(request):
    template_name="blog/humor_toilet.html"
    return render(request,template_name)

def humor_ero(request):
    template_name="blog/humor_ero.html"
    return render(request,template_name)

def humor_lame(request):
    template_name="blog/humor_lame.html"
    return render(request,template_name)

def humor_damage(request):
    template_name="blog/humor_damage.html"
    return render(request,template_name)

def humor_frustrate(request):
    template_name="blog/humor_frustrate.html"
    return render(request,template_name)

def humor_which(request):
    template_name="blog/humor_which.html"
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


def life_comic(request):
    template_name="blog/life_comic.html"
    return render(request,template_name)

def life_english(request):
    template_name="blog/life_english.html"
    return render(request,template_name)

def life_asp(request):
    template_name="blog/life_asp.html"
    return render(request,template_name)


def fashion_glasses(request):
    template_name="blog/fashion_glasses.html"
    return render(request,template_name)


def fashion_summary(request):
    template_name="blog/fashion_summary.html"
    return render(request,template_name)


def fashion_trainer(request):
    template_name="blog/fashion_trainer.html"
    return render(request,template_name)

def fashion_sneaker(request):
    template_name="blog/fashion_sneaker.html"
    return render(request,template_name)

def fashion_jeans(request):
    template_name="blog/fashion_jeans.html"
    return render(request,template_name)

def fashion_auter(request):
    template_name="blog/fashion_auter.html"
    return render(request,template_name)

def fashion_poro(request):
    template_name="blog/fashion_poro.html"
    return render(request,template_name)

def fashion_tshirt(request):
    template_name="blog/fashion_tshirt.html"
    return render(request,template_name)

def fashion_parka(request):
    template_name="blog/fashion_parka.html"
    return render(request,template_name)

def fashion_under(request):
    template_name="blog/fashion_under.html"
    return render(request,template_name)

def fashion_cap(request):
    template_name="blog/fashion_cap.html"
    return render(request,template_name)

def fashion_socks(request):
    template_name="blog/fashion_socks.html"
    return render(request,template_name)

def fashion_watch(request):
    template_name="blog/fashion_watch.html"
    return render(request,template_name)

def fashion_suit(request):
    template_name="blog/fashion_suit.html"
    return render(request,template_name)

def fashion_chino(request):
    template_name="blog/fashion_chino.html"
    return render(request,template_name)

def fashion_skiny(request):
    template_name="blog/fashion_skiny.html"
    return render(request,template_name)

def fashion_tapere(request):
    template_name="blog/fashion_tapere.html"
    return render(request,template_name)

def fashion_cago(request):
    template_name="blog/fashion_cago.html"
    return render(request,template_name)

def fashion_slacks(request):
    template_name="blog/fashion_slacks.html"
    return render(request,template_name)

def fashion_easy(request):
    template_name="blog/fashion_easy.html"
    return render(request,template_name)

def fashion_outer_kinds(request):
    template_name="blog/fashion_outer_kinds.html"
    return render(request,template_name)

def fashion_jacket_kinds(request):
    template_name="blog/fashion_jacket_kinds.html"
    return render(request,template_name)

def fashion_pants_kinds(request):
    template_name="blog/fashion_pants_kinds.html"
    return render(request,template_name)

def fashion_tshirt_kinds_neck(request):
    template_name="blog/fashion_tshirt_kinds_neck.html"
    return render(request,template_name)

def fashion_swimsuit(request):
    template_name="blog/fashion_swimsuit.html"
    return render(request,template_name)

def ads(request):
    template_name="blog/ads.txt"
    return render(request,template_name)