import func as F
import matplotlib.pyplot as plt

# Introduction
# Algoritma K - Nearest Neighbors sederhana


# Dataset 
# setiap row / baris ada 
# [ besarX , besarY , label ]

dataset = [
	[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]


# Tentukan titik yang dicari
# apakah titik ini masuk ke dalam label 0 (nol) atau 1 (satu)
titik = [4.5,3]

# Gambarkan titik tersebut dengan titik berwarna hijau "go"
plt.plot(titik[0],titik[1],"go")

for row in dataset:
    # print(f' {row0} | {row} | {distance} \n\n')

	# Plot kan / gambarkan titik tersebut dengan warna yang berbeda setiap labelnya
	# disini kita plotkan label 1 dengan warna biru dan label 0 dengan warna merah
    if(row[2]==1):
        plt.plot(row[0],row[1],"bo")
    else:
        plt.plot(row[0],row[1],"ro")



plt.ylabel('Y')
plt.xlabel('X')
plt.show()


# Prediksi titik tersebut adalah 0 (nol) atau 1 (satu) 
# Karena label di dataset adalah 0 atau 1
# Nanti bisa jadi labelnya lain seperti "bunga mawar" / "bunga melati"

prediction = F.predict_classification(dataset, titik, 5)
print('Expected %d, Got %d.' % (dataset[0][-1], prediction))