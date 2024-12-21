import pandas as pd

sampah_data = {
    'Kabupaten/Kota': ['Bandung', 'Bekasi', 'Bogor', 'Depok', 'Sukabumi'],
    'Produksi Sampah (Ton)': [5000, 7000, 4500, 3000, 3200],
    'Tahun': [2023, 2023, 2023, 2023, 2023]
}

sampah_df = pd.DataFrame(sampah_data)
print("DataFrame Awal:\n", sampah_df)

total_produksi_2023 = 0
for index, row in sampah_df.iterrows():
    if row['Tahun'] == 2023:
        total_produksi_2023 += row['Produksi Sampah (Ton)']

print("\nTotal Produksi Sampah Tahun 2023:", total_produksi_2023, "Ton")

total_per_tahun = {}
for index, row in sampah_df.iterrows():
    tahun = row['Tahun']
    produksi = row['Produksi Sampah (Ton)']
    if tahun not in total_per_tahun:
        total_per_tahun[tahun] = 0
    total_per_tahun[tahun] += produksi

print("\nJumlah Produksi Sampah Per Tahun:")
for tahun, total in total_per_tahun.items():
    print(f"Tahun {tahun}: {total} Ton")

total_per_kota_tahun = {}
for index, row in sampah_df.iterrows():
    key = (row['Kabupaten/Kota'], row['Tahun'])
    if key not in total_per_kota_tahun:
        total_per_kota_tahun[key] = 0
    total_per_kota_tahun[key] += row['Produksi Sampah (Ton)']

total_per_kota_tahun_df = pd.DataFrame([
    {'Kabupaten/Kota': kota, 'Tahun': tahun, 'Total Produksi Sampah (Ton)': total} 
    for (kota, tahun), total in total_per_kota_tahun.items()
])

print("\nJumlah Produksi Sampah Per Kota/Kabupaten Per Tahun:\n", total_per_kota_tahun_df)

total_per_kota_tahun_df.to_csv('total_per_kota_tahun.csv', index=False)
total_per_kota_tahun_df.to_excel('total_per_kota_tahun.xlsx', index=False)

print("\nData sudah berhasil dibuat dengan sukses.")
