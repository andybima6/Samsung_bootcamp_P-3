"""
1. Buat sebuah program yang jika kita berikan sebuah 
Input = [800,600,400,200]
Compared_input = [500,200,400]
Maka akan menghasilkan output [0,0,1,1]! Usahakan tidak menggunakan list baru!

"""

input = [800,600,400,200]
Compared_input = [500,200,400]

result = []
for i in input:
    if i in Compared_input:
        result.append(1)
    else:
        result.append(0)

print(result)

"""
Jika nilai i terdapat di dalam Compared_input, kita tambahkan nilai 1 ke dalam result menggunakan result.append(1).
Jika nilai i tidak terdapat di dalam Compared_input, kita tambahkan nilai 0 ke dalam result menggunakan result.append(0)
"""

"""
2. Buat sebuah program yang jika kita berikan sebuah 
Input = [100,200,300,400,500]
Compared_input = [500,200,400]
Maka akan menghasilkan output [100,0,300,0,0]! Usahakan tidak menggunakan list baru!

"""
input =  [100,200,300,400,500]
Compared_input = [500,200,400]

result = []

for i in input:
    if i in Compared_input:
        result.append(0)
    else :
        result.append(i)
        
        
print(result)

"""
Jika nilai i terdapat di dalam Compared_input, maka kita tambahkan angka 0 ke dalam result menggunakan result.append(0).
Jika nilai i tidak terdapat di dalam Compared_input, maka kita tambahkan nilai i ke dalam result menggunakan result.append(i).
"""

"""
3. ENUMARATE ADALAH FUNGSI UNTUK MENGRUTKAN INDEX/MEMBACA ADA BERAPA BANYAK INDEX
"""
input = ["A","B","C"]

for index,value in enumerate(input):
    print(index,value)


"""
4. Buat sebuah program dimana jika input yang diberikan adalah 
Input = [
    {‘nama'’': 'Budi',’nilai’: 90},
    {'nama': 'Dwi', ‘nilai’: 85},
    {'nama': 'Tri', ‘nilai’:75},
]
Output = {
“nilai_tertinggi”: “Budi”,
“nilai_terendah”: “Tri”
}

"""
""" cara 1"""
# Input = [
#     {'nama': 'Budi','nilai': 90},
#     {'nama': 'Dwi', 'nilai': 85},
#     {'nama': 'Tri', 'nilai':75},
# ]
# def nilai(list):
#     nilai_tertinggi = max(list, key=lambda x: x['nilai'])
#     nilai_terendah = min(list, key=lambda x: x['nilai'])
#     return{
#         "nilai tertinggi": nilai_tertinggi['nama'],
#         "nilai terendah": nilai_terendah['nama']
#     }

# input = [
#     {'nama':'Budi','nilai':90},
#     {'nama':'Dwi','nilai':85},
#     {'nama':'Tri','nilai':75}
# ]

# result = nilai(input)
# print(result)
""" cara 2"""
# mahasiswa = [
#     {'nama': 'Budi','nilai': 90},
#     {'nama': 'Dwi', 'nilai': 85},
#     {'nama': 'Tri', 'nilai':75},
# ]
# mahasiswa_terbaik = max(mahasiswa,key=lambda x: x["nilai"])
# mahasiswa_krgbaik = min(mahasiswa,key=lambda x: x["nilai"])

# print(mahasiswa_terbaik)
# print(mahasiswa_krgbaik)


"""
5. Buat sebuah program dimana jika input yang diberikan adalah 
Input = [
    {'nama': 'Budi','gaji': 5000},
    {'nama': 'Dwi', 'gaji': 8000},
    {'nama': 'Joko', 'gaji': 6000}
]
Output = {
“highest_salary”: “Dwi”,
“total_salary”: 19000
}
"""
# Input = [
#     {'nama': 'Budi','gaji': 5000},
#     {'nama': 'Dwi', 'gaji': 8000},
#     {'nama': 'Joko', 'gaji': 6000}
# ]

# gaji_tertinggi = 0
# gaji_terendah = 10000
# total = 0

# for data in Input:
#     total += data["gaji"]
#     if gaji_tertinggi < data["gaji"]:
#         nama_gaji_tertinggi = data["nama"]
#         gaji_tertinggi = data["gaji"]
#     if gaji_terendah > data["gaji"]:
#         nama_gaji_terendah = data["nama"]
#         gaji_terendah = data["gaji"]

# output = {
#     "highest_salary": {"nama": nama_gaji_tertinggi, "gaji": gaji_tertinggi},
#     "lowest_salary": {"nama": nama_gaji_terendah, "gaji": gaji_terendah},
#     "total_salary": total
# }

# print(output)

"""
Buat sebuah program dimana jika input yang diberikan adalah

6. 
INput 1:
data_toko = {
    "Indoramet":{
        "Ayam": 30000,
        "Sayur": 15000,
        "Buah": 20000,
        "Ikan": 22000
    }
}

INput 2:
items_to_buy = {
    "Ayam":2,
    "Sayur":1,
    "Ikan":1
}

Output = 97000

Rincian
Ayam : 2 * 30.000 = 60.000
Sayur : 1 * 15.000 = 15.000
Ikan : 1 * 22.000 = 22.000


"""
# data_toko = {
#     "Indomaret": {
#         "Ayam": 30000,
#         "Sayur": 15000,
#         "Buah": 20000,
#         "Ikan": 22000
#     }
# }

# item_to_buy = {
#     "Ayam": 2,
#     "Sayur": 1,
#     "Ikan": 1
# }


""" cara 1"""
# total_cost = 0
# print("Rincian Pembelian:")
# for item, quantity in item_to_buy.items():
#     price_per_item = data_toko["Indomaret"][item]
#     subtotal = price_per_item * quantity
#     print(f"{item}: {quantity} * {price_per_item} = {subtotal}")
#     total_cost += subtotal

# print("\nTotal Biaya: ", total_cost)

""" cara 2"""
# output = 0
# for item in item_to_buy.keys():
#  output += item_to_buy[item] * data_toko["Indomaret"][item]

# print(output)


"""
7. Buat sebuah program dimana jika input yang diberikan adalah 

Hint: Cari harga termurah untuk setiap item antara 2 toko tersebut

Output = 84000

Rincian
Ayam : 2 * 25.000 = 50.000
Sayur : 1 * 12.000 = 12.000
Ikan : 1 * 22.000 = 22.000


"""
# input = {
#     "Indomaret": {
#         "Ayam": 30000,
#         "Sayur": 15000,
#         "Buah": 20000,
#         "Ikan": 22000
#     },
#     "Alfamaret": {
#         "Ayam": 25000,
#         "Sayur": 12000,
#         "Buah": 30000,
#         "Ikan": 25000
#     }
# }

# items_to_buy = {
#     "Ayam": 2,
#     "Sayur": 1,
#     "Ikan": 1
# }
""" cara 1 """
# total_cost = 0
# print("Rincian Pembelian:")
# for item, quantity in items_to_buy.items():
#     if item in input["Indomaret"] and item in input["Alfamaret"]:
#         price_indomaret = input["Indomaret"][item]
#         price_alfamaret = input["Alfamaret"][item]
#         price_per_item = min(price_indomaret, price_alfamaret)
#         subtotal = price_per_item * quantity
#         print(f"{item}: {quantity} * {price_per_item} = {subtotal}")
#         total_cost += subtotal
#     else:
#         print(f"{item} tidak tersedia di salah satu toko.")

# print("\nTotal Biaya: ", total_cost)

""" cara 2 """
# total = 0
# for item, quantity in items_to_buy.items():
"""
item sebagai kunci ("Ayam") dan quantity sebagai nilainya (2).
"""
#     inprice = input["Indomaret"][item]
#     alprice = input["Alfamaret"][item]
#     if inprice < alprice:
#         total += inprice * quantity
#     else:
#         total += alprice * quantity
# print(total)


"""
link coolab : https://www.menti.com/al3u9w4gzqbu """