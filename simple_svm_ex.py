##画像にして出力
#pyplot is used to actually plot a chart
import matplotlib.pyplot as Plt

#datasets are used as a sample dataset, which contains one set that has number recognition data
from sklearn import datasets

#svm is for the sklearn Support Vector Machine
from sklearn import svm

#it is prepared that digits data has 1797 of 64px(8*8), gray scale, handinput image
#so using SVM to classificate 
digits = datasets.load_digits()


###下記はデータフォマットの確認
##actual data
# print (digits.data)
##actual label
# print (digits.target)
# print (digits.images[0])


#specify the classifier=>分類器
#SVC: Support Vector Machine
#ガンマとC二つのパラメータ
#C: どれだけのご分類を許容するか、小さい程誤分類を許容(soft margin)
#ガンマ: RBFカーネルのパラメータ、大きい程境界が複雑になる(trainingには1798のうち60%のデータを使う、40%は検証用)
#digits.targetには各画像の正解データ(数字)が格納されている
#targetプロパティーの中にどの数字を表すかのラsベル情報のリストが入っておりピクセルデータはグレイスケールの8*8で構成されている。
#ピクセルデータは0-15段階の色で表されており、濃い:0-15:薄いとなっている。matplotlibモジュールを使って画像データをピクセルで取得してみる。d
clf = svm.SVC(gamma=0.001, C=100)

print(len(digits.data))

x,y = digits.data[:-10], digits.target[:-10]
clf.fit(x, y)

print('Prediction:', clf.predict(digits.data[-2]))

Plt.imshow(digits.images[-2], cmap=Plt.cm.gray_r, interpolation="nearest")
Plt.show()