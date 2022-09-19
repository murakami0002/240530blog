# インスタンスとは・・・クラスは設計図、インスタンスは設計図から実際に作られたモノ
# インスタンスは固有の変数を持つことができ、この変数をインスタンス変数という。
# オブジェクト　＝　インスタンス
# インスタンス変数、インスタンス、オブジェクト、クラス
# イメージ：インスタンス変数（下の例で田中、加藤など）がフィールド名、カラム名に当たる。インスタン変数の呼び出しが、フィールド名、カラム名の呼び出し。

"""
インスタンス変数の宣言
class クラス:
 def __init__(self,変数,...)
 self.変数 = 引数　　
 コンストラクタinitで宣言する変数がインスタンス変数
"""

"""
インスタンス変数の値にアクセスする方法
インスタンスを生成して、インスタンス（インスタンスが格納された変数）を介してインスタンス変数にアクセスできる。
□クラスの外からアクセスする方法
インスタンス名（インスタンスが格納された変数）の後にアクセスしたいインスタンス変数を記述する。
インスタンス名.インスタンス変数名

例
class Sample:
    def __init__(self,name):
        self.name = name

#インスタンスの生成
sample1 = Sample("田中")
sample2 = Sample("加藤")

#インスタンス変数の呼び出し
print('sample1：',sample1.name)
print('sample2：',sample2.name)

例の結果
sample1： 田中
sample2： 加藤

□クラスの内部（他のメソッド）からアクセスする方法
書式
class クラス名:

    def __init__(self,引数①,引数②,…):
        self.インスタンス変数① = 引数①
        self.インスタンス変数② = 引数②
        …
    def メソッド名(self)
        print(self.インスタンス変数①)
        print(self.インスタンス変数②)
例
class Sample: 
    def __init__(self,name1,name2):
        self.name1 = name1
        self.name2 = name2

    def callName(self):
        print('名前①：',self.name1)
        print('名前②：',self.name2)

#インスタンスの生成
sample1 = Sample('田中','加藤')

#メソッドを介してインスタンス変数の呼び出し
sample1.callName()

結果
名前①： 田中
名前②： 加藤
"""

"""
class Circle:
    def __init__(self, radius):
        # インスタンス変数に値を代入
        self.radius = radius

    # 関数を定義
    def area(self):
        return radius * radius * 3.14


radius = 10
# インスタンスの生成
# インスタンスを生成して、circleという変数に代入。
circle = Circle(radius)


print("円の半径:", radius)
print("円の面積:", circle.area())
"""

"""
class Sample:
    def __init__(self,name):
        self.name = name

#インスタンスの生成
sample1 = Sample("田中")
sample2 = Sample("加藤")

#インスタンス変数の呼び出し
print('sample1：',sample1.name)
print('sample2：',sample2.name)
"""