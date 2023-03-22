# API Cek 📑🗓

"Cek tagihan" adalah sebuah istilah yang merujuk pada proses memeriksa jumlah uang yang harus dibayarkan oleh seseorang
atas layanan atau produk yang telah diberikan oleh pihak lain. Biasanya, tagihan ini berisi rincian mengenai jenis
layanan atau produk yang digunakan, jumlah yang harus dibayar, dan tanggal jatuh tempo pembayaran. Dengan melakukan "cek
tagihan", seseorang dapat memastikan bahwa tagihan yang diterima sesuai dengan layanan atau produk yang telah digunakan.
Dibuat menggunakan bahasa pemrograman Python3 dan metode scraping. Scraping adalah teknik ekstraksi data yang dilakukan
dengan cara mengambil informasi dari sebuah website bukalapak secara otomatis, menggunakan library atau framework
tertentu

Project ini dibuat untuk tujuan pengembangan dan pembelajaran

## Library

- [Requests](https://pypi.org/project/requests/)
- [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [Requests-toolbelt](https://pypi.org/project/requests-toolbelt/)
- [Fake_useragent](https://pypi.org/project/fake-useragent/)

## Fitur

| Nama                                    | Status |
|-----------------------------------------|--------|
| prepaidInquiries ( Token Listrik )      | ✅      |
| postpaidInquiries ( Tagihan Listrik )   | ✅      |
| pdamInquiries ( Tagihan PDAM )          | ✅      |
| bpjsKesehatanInquiries ( Tagihan BPJS ) | ✅      |

## Cara Penggunaan

```python
# Import library untuk mengecek tagihan listrik prabayar
from src.prepaidInquiries import prepaidInquiries

# panggil class prepaidInquiries dan method _get_data()
# parameter pertama adalah customer_number (nomor pelanggan)

print(
    prepaidInquiries(
        customer_number="xxxxxxxxxxx"
    )._get_data()
)

# contoh output jika berhasil
# {
#     "status": True,
#     "customer_number": "xxxxxx",
#     "customer_name": "x xxxx xxxxxx",
#     "segmentation": "R1",
#     "power": 2200
# }

# contoh output jika gagal
# {
#    "status": False,
#    "customer_number": "xxxxxx"
# }
```

## Refrensi 

### Prepaid Inquiries

Prepaid Inquiries adalah sebuah function yang digunakan untuk mengecek tagihan listrik prabayar

| Parameter       | Tipe Data | Keterangan      |
|-----------------|-----------|-----------------|
| customer_number | String    | Nomor pelanggan |

Contoh output jika berhasil

```json
{
  "status": true,
  "customer_number": "xxxxxx",
  "customer_name": "x xxxx xxxxxx",
  "segmentation": "R1",
  "power": 2200
}
```

Contoh output jika gagal

```json
{
  "status": false,
  "customer_number": "xxxxxx"
}
```

### Postpaid Inquiries

Postpaid Inquiries adalah sebuah function yang digunakan untuk mengecek tagihan listrik pascabayar

| Parameter       | Tipe Data | Keterangan      |
|-----------------|-----------|-----------------|
| customer_number | String    | Nomor pelanggan |

Contoh output jika berhasil

```json
{
  "status": true,
  "customer_number": "xxxxxx",
  "customer_name": "xxxxx xxxxxx",
  "segmentation": "R1",
  "power": 450,
  "period": [
    "2023-03-01"
  ],
  "stand_meter": "00015338 - 00015445",
  "amount": 52230
}
```

Contoh output jika gagal

```json
{
  "status": false,
  "customer_number": "xxxxxx",
  "message": "Nomor tidak terdaftar"
}
```

### PDAM Inquiries

PDAM Inquiries adalah sebuah function yang digunakan untuk mengecek tagihan PDAM

| Parameter       | Tipe Data | Keterangan      |
|-----------------|-----------|-----------------|
| customer_number | String    | Nomor pelanggan |
| operator_id     | String    | ID operator     |

Contoh output jika berhasil

```json
{
  "status": true,
  "customer_number": "xxxxxx",
  "customer_name": "xxxxx xxxxxx",
  "bills": [
    {
      "usage": "0000013780",
      "start_meter": 486000,
      "end_meter": 499780,
      "address": "-",
      "admin_fee": 3000,
      "penalty_fee": 5000,
      "bill_period": "2023-02-01",
      "amount": 73156,
      "cubication": "486000-499780"
    }
  ]
}
```

Contoh output jika gagal

```json
{
  "status": false,
  "customer_number": "xxxxxx",
  "message": "Tagihan tidak ditemukan atau sudah dibayar"
}
```

Mengambil ID operator

Data telah di sort berdasarkan group

```python
from src.pdamInquiries import pdamInquiries

print(
    pdamInquiries("xxxx")._get_operators()
)

# Output
# {
#     "status": true,
#     "data": [
#         {
#             "id": 471,
#             "name": "PDAM  Kota Banda Aceh",
#             "group": "Aceh"
#         },
#         {
#             "id": 486,
#             "name": "PDAM Kab. Aceh Barat",
#             "group": "Aceh"
#         },
#         .. dan seterusnya
#     ]
# }
```

### BPJS Kesehatan Inquiries

BPJS Kesehatan Inquiries adalah sebuah function yang digunakan untuk mengecek tagihan BPJS Kesehatan

| Parameter       | Tipe Data | Keterangan      |
|-----------------|-----------|-----------------|
| customer_number | String    | Nomor pelanggan |

Contoh output jika berhasil

```json
{
  "status": true,
  "customer_number": "xxxxxx",
  "customer_name": "xxxxx xxxxxx",
  "count_family_members": 4,
  "amount": 142500
}
```

Contoh output jika gagal

```json
{
  "status": false,
  "customer_number": "0000003137160351",
  "message": "Tagihan tidak ditemukan atau sudah dibayar"
}
```


