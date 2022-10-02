from django.urls import path
#djangoモジュールのurlsクラスのpath関数をimport

from . import views


app_name='blog'
#他のアプリで
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
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
    path('what_life',views.whatlife,name='what_life'),
    path('life_summary',views.life_summary,name='life_summary'),
    path('tsukkomi',views.tsukkomi,name='tsukkomi'),
    path('trivia_summary',views.trivia_summary,name='trivia_summary'),
    path('trivia_rich',views.trivia_rich,name='trivia_rich'),
    path('trivia_athlete_rich',views.trivia_athlete_rich,name='trivia_athlete_rich'),
    path('trivia_artist_rich',views.trivia_artist_rich,name='trivia_artist_rich'),
    path('trivia_soccer_goal',views.trivia_soccer_goal,name='trivia_soccer_goal'),
    path('trivia_comedian',views.trivia_comedian,name='trivia_comedian'),
    path('party_game',views.party_game,name='party_game'),
]