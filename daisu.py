#乱数生成用ライブラリ
import random
#数学計算用ライブラリ
import math

#試行回数を設定
max_try = int(input('最大試行回数を入力してください（10を入力値でべき乗) :\n'))
#パターンを設定
pattern = int(input('何分の1を計算するのか入力してください : \n'))
#理論的な確率を計算
theory = (1 / pattern) * 100
print(theory)

print('\n{0}通りの数のうち1が出る確率は理論上{1}%\n'.format(pattern,theory))
print('計算スタート!!\n')

for i in range(1,max_try) :
    #試行回数を設定
    try_num = pow(10,i)
    #countを初期化
    count = 0

    for x in range(try_num):
        #乱数生成
        dice = random.randint(1,pattern)
        #1を判定
        if dice == 1 :
            count += 1
    # 確率を計算
    result = (count / try_num) * 100
    # 結果を印字
    out = '{0}回で1が出る確率は{1}%  理論値との差は{2}%'.format(try_num,result,math.fabs(result - theory))
    print(out)
