from django.urls import path
#djangoモジュールのurlsクラスのpath関数をimport

from . import views


app_name='blog'
#他のアプリで
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    #path('top_page',views.top_page,name='top_page'),
    #pathは関数、path(URL,関数またはクラス、name=URL名称）
    #nameで指定したURL名称は主に以下３つのパターンで使用される。
    #name関数を使うメリットはURLを変更しても、他ファイルの変更必要なし
    #1.テンプレート：aタグのhref属性で指定
    #2.views.py:redirectで使用
    #3.views.py:reverseで使用
    #path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    #path(int整数の型を定義、実行する関数,name＝URL名称）
    #URLに数字を入力する→urlpatternsと一致する引数を探す→隣の関数を呼び出す→関数内の動作を実施する
    #path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),
    #path('<int:question_id>/vote/',views.vote,name='vote'),
    path('trivia_greatman',views.trivia_greatman,name='trivia_greatman'),
    path('life_summary',views.life_summary,name='life_summary'),
    path('life_fx',views.life_fx,name='life_fx'),
    path('trivia_summary',views.trivia_summary,name='trivia_summary'),
    path('trivia_rich',views.trivia_rich,name='trivia_rich'),
    path('trivia_athlete_rich',views.trivia_athlete_rich,name='trivia_athlete_rich'),
    path('trivia_artist_rich',views.trivia_artist_rich,name='trivia_artist_rich'),
    path('trivia_soccer_goal',views.trivia_soccer_goal,name='trivia_soccer_goal'),
    path('trivia_comedian',views.trivia_comedian,name='trivia_comedian'),
    path('trivia_game',views.trivia_game,name='trivia_game'),
    path('trivia_baseball_homerun',views.trivia_baseball_homerun,name='trivia_baseball_homerun'),
    path('trivia_potatochips',views.trivia_potatochips,name='trivia_potatochips'),
    path('trivia_population',views.trivia_population,name='trivia_population'),
    path('trivia_athlete_rich2',views.trivia_athlete_rich,name='trivia_athlete_rich2'),
    path('trivia_game',views.trivia_game,name='trivia_game'),
    path('diary_230110',views.diary_230110,name='diary_230110'),
    path('diary_summary',views.diary_summary,name='diary_summary'),
    path('diary_230114',views.diary_230114,name='diary_230114'),
    path('diary_230115',views.diary_230115,name='diary_230115'),
    path('humor_summary',views.humor_summary,name='humor_summary'),
    path('humor_seiza',views.humor_seiza,name='humor_seiza'),
    path('humor_busaiku',views.humor_busaiku,name='humor_busaiku'),
    path('humor_ladytalk',views.humor_ladytalk,name='humor_ladytalk'),
    path('humor_party',views.humor_party,name='humor_party'),
    path('humor_smart',views.humor_smart,name='humor_smart'),
    path('humor_macchan',views.humor_macchan,name='humor_macchan'),
    path('humor_propose',views.humor_propose,name='humor_propose'),
    path('humor_nickname',views.humor_nickname,name='humor_nickname'),
    path('humor_yourself',views.humor_yourself,name='humor_yourself'),
    path('humor_positive',views.humor_positive,name='humor_positive'),
    path('humor_life',views.humor_life,name='humor_life'),
    path('humor_soccer_tsukkomi',views.humor_soccer_tsukkomi,name='humor_soccer_tsukkomi'),
    path('humor_baseball_tsukkomi',views.humor_baseball_tsukkomi,name='humor_baseball_tsukkomi'),
    path('life_kabu',views.life_kabu,name='life_kabu'),
    path('life_coin',views.life_coin,name='life_coin'),
    path('life_comic',views.life_comic,name='life_comic'),
    path('life_english',views.life_english,name='life_english'),

]