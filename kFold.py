"""
------- INFORMASI -------
NB: install pandas atau anaconda sebelum menjalankan file ini

file ini digunakan untuk mencari k
range k yang dicari mulai dari 0 hingga 3200
proses ini memakan waktu yang sangat lama
"""
import pandas as pd
import math

from collections import Counter

k_fold = 5
df_train = pd.read_excel("dataset_fix.xlsx", "DataTrain")
if __name__ == '__main__':
    for k_value in range(0,3200,2):
        print(k_value)
        sum_accuracy = 0
        start_val = 0
        finish_val = 800
        while (start_val < 4000):
            accuracy = 0
            # i for data train, j for data test
            for i in range(start_val,finish_val):
                like = df_train.loc[i, "Like"]
                provokasi = df_train.loc[i, "Provokasi"]
                komentar = df_train.loc[i, "Komentar"]
                emosi = df_train.loc[i, "Emosi"]

                euclid_val = []
                for j in range(len(df_train)):
                    if (not (j>=start_val and j<=finish_val)):
                        value = math.sqrt(((like - df_train.loc[j, "Like"]) ** 2) + (
                                                (provokasi - df_train.loc[j, "Provokasi"]) ** 2) + (
                                                (komentar - df_train.loc[j, "Komentar"]) ** 2) + (
                                                (emosi - df_train.loc[j, "Emosi"]) ** 2))
                        euclid_val.append(value)
                euclid_val_sorted = sorted(euclid_val)
                nearest_neighbor = []
                for k in range(k_value):
                    nearest_neighbor.append(df_train.loc[euclid_val.index(euclid_val_sorted[k]), "Hoax"])
                counter = Counter(nearest_neighbor)
                if (counter.most_common()[0][0] == df_train.loc[i, "Hoax"]):
                    accuracy += 1
            sum_accuracy += ((accuracy/800) * 100)
            start_val += 800
            finish_val += 800
        print("Akurasi dengan k-"+str(k_value)+": "+str(sum_accuracy/k_fold))