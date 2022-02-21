#print("Hello Python in Visual Studio2019")
#a = 1 + 2
#print(a)

#import sys
#from math import cos,radians

#for i in range(360):
#    print(cos(radians(i)))

#a = 1
#print(a)
#a = a + 1
#print(a)

#a = 1
#b = 1/2
#c = "ABC"
#print(a)
#print(b)
#print(c)
#print(type(a))
#print(type(b))
#print(type(c))

#a = 1
#b = 2
#print(id(a),id(b))

##xの平方根を求める
#x = 2
##
#rnew = x
##
#r1 = rnew
#r2 = x / r1
#rnew = (r1 + r2) / 2
#print(r1,rnew,r2)
##
#r1 = rnew
#r2 = x / r1
#rnew = (r1 + r2) / 2
#print(r1,rnew,r2)
##
#r1 = rnew
#r2 = x / r1
#rnew = (r1 + r2) / 2
#print(r1,rnew,r2)
#↓以下for文
#x = 2
#rnew = 2
#for i in range(10):
#    r1 = rnew
#    r2 = x/r1
#    rnew = (r1 + r2) / 2
#print(r1,rnew,r2)

#for i in range(10):
#    if i == 1:
#        continue
#    if i == 8:
#        break
#    print(i)

#forの入れ子
#for i in range(3):
#    for j in range(3):
#        print(i,j)

#for i in["三条","四条","五条"]:
#    for j in["河原町","烏丸","堀川"]:
#        cross = i + j
#        print(cross)

#while
#x = 2
#rnew = x
#diff = rnew - x / rnew #絶対値
#if(diff<0):
#    diff = -diff
##差が10マイナス6乗より大きければ繰り返す
#while(diff > 1.0E-6):
#    r1 = rnew
#    r2 = x/r1
#    rnew = (r1 + r2) / 2
#    print(r1,rnew,r2)
##差の再計算
#    diff = r1 - r2
#    if(diff < 0):
#        diff = -diff

#while True:
#    x = input("正の値を入力してください")
#    try:#エラーが生じるところをこのブロックに入れる
#        x = float(x)
#    except ValueError:
#        print(x,"は数値に変換できません")
#        continue
#    except:
#        print("予期せぬエラーです")
#        exit()
#    if(x <= 0):
#        print(x,"は正の値ではありません")
#        continue
#    #正しい入力が行われた時
#    print(x)

##
#def square_root(x):
#    '引数xの平方根を求める'
#    rnew = x
#    #
#    diff = rnew - x / rnew
#    if(diff < 0):
#        diff = -diff
#    while(diff > 1.0E-6):
#        r1 = rnew
#        r2 = x / r1
#        rnew = (r1 + r2) / 2
#        print(r1,rnew,r2)
#        diff = r1 - r2
#        if(diff < 0):
#            diff = -diff
#            #値を返す
#    return rnew
##ここからメイン
#    v = 2
#    r = square_root(v)
#    print("結果は",r)