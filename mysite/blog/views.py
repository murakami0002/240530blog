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

"""def Top(request):
    template_name="blog/Top.html"
    return render(request,template_name)"""

"""class IndexView(generic.ListView):
    template_name = "blog/Work.html"
    context_object_name='latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
"""
class IndexView(generic.ListView):
    template_name = "blog/Top.html"
    context_object_name='latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

"""def top_page(request):
    template_name="Work.html"
    return render(request,template_name)"""

def trivia_break(request):
    template_name="blog/trivia_break.html"
    return render(request,template_name)

def trivia_break1(request):
    template_name="blog/trivia_break1.html"
    return render(request,template_name)


def trivia_greatman(request):
    template_name="blog/trivia_greatman.html"
    return render(request,template_name)

def trivia_greatman1(request):
    template_name="blog/trivia_greatman1.html"
    return render(request,template_name)


def life_summary1(request):
    template_name="blog/life_summary1.html"
    return render(request,template_name)

def trivia_summary(request):
    template_name="blog/trivia_summary.html"
    return render(request,template_name)

def trivia_summary1(request):
    template_name="blog/trivia_summary1.html"
    return render(request,template_name)


def trivia_rich1(request):
    template_name="blog/trivia_rich1.html"
    return render(request,template_name)

def trivia_athlete_rich1(request):
    template_name="blog/trivia_athlete_rich1.html"
    return render(request,template_name)

def trivia_artist_rich(request):
    template_name="blog/trivia_artist.html"
    return render(request,template_name)

def trivia_artist_rich1(request):
    template_name="blog/trivia_artist1.html"
    return render(request,template_name)

def trivia_soccer_goal1(request):
    template_name="blog/trivia_soccer_goal1.html"
    return render(request,template_name)


def trivia_comedian1(request):
    template_name="blog/trivia_comedian1.html"
    return render(request,template_name)


def trivia_game(request):
    template_name="blog/trivia_game.html"
    return render(request,template_name)

def trivia_game1(request):
    template_name="blog/trivia_game1.html"
    return render(request,template_name)


def trivia_baseball_homerun1(request):
    template_name="blog/trivia_baseball_homerun1.html"
    return render(request,template_name)


def trivia_potatochips1(request):
    template_name="blog/trivia_potatochips1.html"
    return render(request,template_name)

def trivia_population1(request):
    template_name="blog/trivia_population1.html"
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

def humor_summary0(request):
    template_name="blog/humor_summary0.html"
    return render(request,template_name)

def humor_summary1(request):
    template_name="blog/humor_summary1.html"
    return render(request,template_name)

def humor_summary2(request):
    template_name="blog/humor_summary2.html"
    return render(request,template_name)

def humor_summary3(request):
    template_name="blog/humor_summary3.html"
    return render(request,template_name)

def humor_summary4(request):
    template_name="blog/humor_summary4.html"
    return render(request,template_name)

def humor_summary5(request):
    template_name="blog/humor_summary5.html"
    return render(request,template_name)

def humor_summary6(request):
    template_name="blog/humor_summary6.html"
    return render(request,template_name)

def humor_seiza1(request):
    template_name="blog/humor_seiza1.html"
    return render(request,template_name)

def humor_cool1(request):
    template_name="blog/humor_cool1.html"
    return render(request,template_name)


def humor_busaiku1(request):
    template_name="blog/humor_busaiku1.html"
    return render(request,template_name)


def humor_ladytalk1(request):
    template_name="blog/humor_ladytalk1.html"
    return render(request,template_name)


def humor_party1(request):
    template_name="blog/humor_party1.html"
    return render(request,template_name)



def humor_smart1(request):
    template_name="blog/humor_smart1.html"
    return render(request,template_name)


def humor_macchan1(request):
    template_name="blog/humor_macchan1.html"
    return render(request,template_name)


def humor_propose1(request):
    template_name="blog/humor_propose1.html"
    return render(request,template_name)


def humor_nickname1(request):
    template_name="blog/humor_nickname1.html"
    return render(request,template_name)


def humor_yourself1(request):
    template_name="blog/humor_yourself1.html"
    return render(request,template_name)


def humor_positive1(request):
    template_name="blog/humor_positive1.html"
    return render(request,template_name)


def humor_life1(request):
    template_name="blog/humor_life1.html"
    return render(request,template_name)


def humor_soccer_tsukkomi1(request):
    template_name="blog/humor_soccer_tsukkomi1.html"
    return render(request,template_name)

def humor_baseball_tsukkomi1(request):
    template_name="blog/humor_baseball_tsukkomi1.html"
    return render(request,template_name)


def humor_fart1(request):
    template_name="blog/humor_fart1.html"
    return render(request,template_name)


def humor_nosehair1(request):
    template_name="blog/humor_nosehair1.html"
    return render(request,template_name)


def humor_badbreath1(request):
    template_name="blog/humor_badbreath1.html"
    return render(request,template_name)


def humor_bodyodor1(request):
    template_name="blog/humor_bodyodor1.html"
    return render(request,template_name)

def humor_footodor1(request):
    template_name="blog/humor_footodor1.html"
    return render(request,template_name)


def humor_booger1(request):
    template_name="blog/humor_booger1.html"
    return render(request,template_name)


def humor_silent1(request):
    template_name="blog/humor_silent1.html"
    return render(request,template_name)


def humor_boss1(request):
    template_name="blog/humor_boss1.html"
    return render(request,template_name)


def humor_junior1(request):
    template_name="blog/humor_junior1.html"
    return render(request,template_name)


def humor_reunion1(request):
    template_name="blog/humor_reunion1.html"
    return render(request,template_name)


def humor_makeup1(request):
    template_name="blog/humor_makeup1.html"
    return render(request,template_name)

def humor_parent1(request):
    template_name="blog/humor_parent1.html"
    return render(request,template_name)


def humor_friends1(request):
    template_name="blog/humor_friends1.html"
    return render(request,template_name)


def humor_toilet1(request):
    template_name="blog/humor_toilet1.html"
    return render(request,template_name)


def humor_ero1(request):
    template_name="blog/humor_ero1.html"
    return render(request,template_name)


def humor_lame1(request):
    template_name="blog/humor_lame1.html"
    return render(request,template_name)


def humor_damage1(request):
    template_name="blog/humor_damage1.html"
    return render(request,template_name)


def humor_frustrate1(request):
    template_name="blog/humor_frustrate1.html"
    return render(request,template_name)


def humor_which1(request):
    template_name="blog/humor_which1.html"
    return render(request,template_name)


def humor_love1(request):
    template_name="blog/humor_love1.html"
    return render(request,template_name)


def humor_reason1(request):
    template_name="blog/humor_reason1.html"
    return render(request,template_name)


def humor_type1(request):
    template_name="blog/humor_type1.html"
    return render(request,template_name)


def humor_blood1(request):
    template_name="blog/humor_blood1.html"
    return render(request,template_name)


def humor_like1(request):
    template_name="blog/humor_like1.html"
    return render(request,template_name)


def humor_cinema1(request):
    template_name="blog/humor_cinema1.html"
    return render(request,template_name)


def humor_deny1(request):
    template_name="blog/humor_deny1.html"
    return render(request,template_name)


def humor_hobby1(request):
    template_name="blog/humor_hobby1.html"
    return render(request,template_name)


def humor_fetish1(request):
    template_name="blog/humor_fetish1.html"
    return render(request,template_name)


def humor_bye1(request):
    template_name="blog/humor_bye1.html"
    return render(request,template_name)


def humor_late1(request):
    template_name="blog/humor_late1.html"
    return render(request,template_name)


def humor_job1(request):
    template_name="blog/humor_job1.html"
    return render(request,template_name)


def humor_holiday1(request):
    template_name="blog/humor_holiday1.html"
    return render(request,template_name)


def humor_birthplace1(request):
    template_name="blog/humor_birthplace1.html"
    return render(request,template_name)


def humor_dream1(request):
    template_name="blog/humor_dream1.html"
    return render(request,template_name)


def humor_deep1(request):
    template_name="blog/humor_deep1.html"
    return render(request,template_name)


def humor_thoughts1(request):
    template_name="blog/humor_thoughts1.html"
    return render(request,template_name)


def humor_stress1(request):
    template_name="blog/humor_stress1.html"
    return render(request,template_name)


def humor_lookup1(request):
    template_name="blog/humor_lookup1.html"
    return render(request,template_name)


def humor_artist1(request):
    template_name="blog/humor_artist1.html"
    return render(request,template_name)


def humor_sports1(request):
    template_name="blog/humor_sports1.html"
    return render(request,template_name)


def humor_flash1(request):
    template_name="blog/humor_flash1.html"
    return render(request,template_name)


def humor_salary11(request):
    template_name="blog/humor_salary11.html"
    return render(request,template_name)

def humor_salary12(request):
    template_name="blog/humor_salary12.html"
    return render(request,template_name)

def humor_salary13(request):
    template_name="blog/humor_salary13.html"
    return render(request,template_name)

def humor_salary14(request):
    template_name="blog/humor_salary14.html"
    return render(request,template_name)


def life_fx1(request):
    template_name="blog/life_fx1.html"
    return render(request,template_name)


def life_kabu1(request):
    template_name="blog/life_kabu1.html"
    return render(request,template_name)



def life_coin1(request):
    template_name="blog/life_coin1.html"
    return render(request,template_name)


def life_comic1(request):
    template_name="blog/life_comic1.html"
    return render(request,template_name)


def life_english1(request):
    template_name="blog/life_english1.html"
    return render(request,template_name)

def life_asp1(request):
    template_name="blog/life_asp1.html"
    return render(request,template_name)


def fashion_glasses1(request):
    template_name="blog/fashion_glasses1.html"
    return render(request,template_name)


def fashion_summary1(request):
    template_name="blog/fashion_summary1.html"
    return render(request,template_name)

def fashion_summary2(request):
    template_name="blog/fashion_summary2.html"
    return render(request,template_name)


def fashion_summary3(request):
    template_name="blog/fashion_summary3.html"
    return render(request,template_name)


def fashion_trainer1(request):
    template_name="blog/fashion_trainer1.html"
    return render(request,template_name)


def fashion_sneaker1(request):
    template_name="blog/fashion_sneaker1.html"
    return render(request,template_name)


def fashion_jeans1(request):
    template_name="blog/fashion_jeans1.html"
    return render(request,template_name)


def fashion_auter1(request):
    template_name="blog/fashion_auter1.html"
    return render(request,template_name)


def fashion_poro1(request):
    template_name="blog/fashion_poro1.html"
    return render(request,template_name)



def fashion_tshirt1(request):
    template_name="blog/fashion_tshirt1.html"
    return render(request,template_name)



def fashion_parka1(request):
    template_name="blog/fashion_parka1.html"
    return render(request,template_name)



def fashion_under1(request):
    template_name="blog/fashion_under1.html"
    return render(request,template_name)



def fashion_cap1(request):
    template_name="blog/fashion_cap1.html"
    return render(request,template_name)



def fashion_socks1(request):
    template_name="blog/fashion_socks1.html"
    return render(request,template_name)



def fashion_watch1(request):
    template_name="blog/fashion_watch1.html"
    return render(request,template_name)



def fashion_suit1(request):
    template_name="blog/fashion_suit1.html"
    return render(request,template_name)


def fashion_chino1(request):
    template_name="blog/fashion_chino1.html"
    return render(request,template_name)


def fashion_skiny1(request):
    template_name="blog/fashion_skiny1.html"
    return render(request,template_name)


def fashion_tapere1(request):
    template_name="blog/fashion_tapere1.html"
    return render(request,template_name)


def fashion_cago1(request):
    template_name="blog/fashion_cago1.html"
    return render(request,template_name)


def fashion_slacks1(request):
    template_name="blog/fashion_slacks1.html"
    return render(request,template_name)


def fashion_easy1(request):
    template_name="blog/fashion_easy1.html"
    return render(request,template_name)


def fashion_outer_kinds1(request):
    template_name="blog/fashion_outer_kinds1.html"
    return render(request,template_name)


def fashion_jacket_kinds1(request):
    template_name="blog/fashion_jacket_kinds1.html"
    return render(request,template_name)


def fashion_pants_kinds1(request):
    template_name="blog/fashion_pants_kinds1.html"
    return render(request,template_name)


def fashion_tshirt_kinds_neck1(request):
    template_name="blog/fashion_tshirt_kinds_neck1.html"
    return render(request,template_name)


def fashion_swimsuit1(request):
    template_name="blog/fashion_swimsuit1.html"
    return render(request,template_name)

def ads(request):
    template_name="blog/ads.txt"
    return render(request,template_name)