"""
ini adalah project demo pertama saya dengan python
"""
print("Hello word")
print("myname is Aji")

"""
semua sintaksis dasar pemrograman terdiri dari:
1.sekuensial : langkah berurutan
2.percabangan : langkah melompat jika kondisi terpenuhi
3. Perulangan : mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""
# skuensial
print('ibu berkata,"pergi ke toko"')
print('Anak menjawab, "Baik,apa yang harus saya lakukan di toko "')
print('Ibu menjawab,"Beli satu botol susu, jika ada telor beli 6 "')
print("maka Anak pergi  ke toko")
print("dan mulai berbelanja")

# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL: Eksekusi berurutan
print('Hello World!')
print('by EKO')
print('Tanggal 10 Juni 2020')
print('-' * 10)

# PERCABANGAN: Eksekusi terpilih
ingin_cepat = False
if ingin_cepat:
    print('jalan lurus aja ya!')
else:
    print('Jalan lain')

# PERULANGAN
jumlah_anak = 4

for index_anak in range(1, jumlah_anak+1): #jumlah perulangan = 5 - 1 = 4
    print(f'Halo anak #{index_anak}')