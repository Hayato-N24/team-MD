
import pickle
import MeCab
import numpy as np
from sklearn.naive_bayes import GaussianNB


# ファイル名
data_file = "app/word_dic.pickle"
model_file = "app/check_model.pickle"
label_names = ['OK', 'OUT']
# 単語辞書を読み出す --- (※2)
data = pickle.load(open(data_file, "rb"))
word_dic = data[2]
# MeCabの準備
tagger = MeCab.Tagger()
# 学習済みモデルを読み出す --- (※3)
model = pickle.load(open(model_file, "rb"))

# テキストがスパムかどうか判定する --- (※4)
def checkTweet(text):
    # テキストを単語IDのリストに変換し単語の頻出頻度を調べる
    zw = np.zeros(word_dic['__id'])
    count = 0
    s = tagger.parse(text)
    # 単語毎の回数を加算 --- (※5)
    for line in s.split("\n"):
        if line == "EOS": break
        org =  line.split(",")[6]# 単語の原型
        if org in word_dic:
            id = word_dic[org]
            zw[id] += 1
            count += 1
    zw = zw / count #  --- (※6)
    # 予測
    pre = model.predict([zw])[0]#  --- (※7)
    return label_names[pre]
