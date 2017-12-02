"""
------- INFORMASI -------
NB: install pandas atau anaconda sebelum menjalankan file ini

file ini digunakan untuk menjawab sheet DataTest dan mengoutputkan ke file output.xlsx
mohon sabar menunggu hingga proses selesai
"""

import math
import pandas as pd
from collections import Counter

df_train = pd.read_excel("dataset_fix.xlsx", "DataTrain")
df_test = pd.read_excel("dataset_fix.xlsx", "DataTest")

if __name__ == '__main__':
    k_value = 201
    accuracy = 0
    result = []
    print(df_test.head())
    # i for data train, j for data test
    for i in range(len(df_test)):
        euclid_val = []
        like = df_test.loc[i, "Like"]
        provokasi = df_test.loc[i, "Provokasi"]
        komentar = df_test.loc[i, "Komentar"]
        emosi = df_test.loc[i, "Emosi"]

        for j in range(len(df_train)):
            value = math.sqrt(((like - df_train.loc[j, "Like"]) ** 2) + (
                    (provokasi - df_train.loc[j, "Provokasi"]) ** 2) + (
                                      (komentar - df_train.loc[j, "Komentar"]) ** 2) + (
                                      (emosi - df_train.loc[j, "Emosi"]) ** 2))
            euclid_val.append(value)
        euclid_val_sorted = sorted(euclid_val)
        nearest_neighbours = []
        for j in range(k_value):
            nearest_neighbours.append(df_train.loc[euclid_val.index(euclid_val_sorted[j]), "Hoax"])
        counter = Counter(nearest_neighbours)
        df_test.loc[i, "Hoax"] = counter.most_common()[0][0]

    print(df_test.head())
    writer = pd.ExcelWriter("output.xlsx", engine="xlsxwriter")
    df_test.to_excel(writer, index=False, sheet_name="Result")
    writer.save()
