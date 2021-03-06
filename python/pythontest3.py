class Shopping_test:
    # 定数を定義
    apple_price = int(200)

    # コンストラクタ（初期化メソッド）
    def __init__(self, username):
        self.username = username

    def shopping(self, money, count):
        total_price = Shopping_test.apple_price * count
        # print(self.username + 'が購入' + '購入するりんごの個数は' + str(count) + '個です\n'
        #       + '支払い金額は' + str(total_price) + '円です')
        print('{}が購入\n購入するリンゴの個数は{}個です\n支払い金額は{}円です'
        .format(self.username,str(count),str(total_price)))

        if money > total_price:
            # print('りんごを' + str(count) + '個買いました'
            #       + '残金は' + str(money - total_price) + '円です\n')
            print('りんごを{}個買いました、残金は{}円です\n'
            .format(str(count),str(money - total_price)))
        elif money == total_price:
            # print('りんごを' + str(count) + '個買いました\n'
            #       + '財布が空になりました\n')
            print('りんごを{}個買いました、財布が空になりました'
            .format(str(count)))
        else:
            print('お金が足りません\nりんごを買えませんでした\n')

member1 = Shopping_test(input('名前を入力：'))  # インスタンスを生成（実体化）
member1.shopping(int(input('所持金を入力：')), int(input('購入するリンゴの個数を入力：')))

member2 = Shopping_test(input('名前を入力：'))  # インスタンスを生成（実体化)
member2.shopping(int(input('所持金を入力：')), int(input('購入するリンゴの個数を入力：')))
