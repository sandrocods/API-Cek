
# API Cek 📑🗓

"Cek tagihan" adalah sebuah istilah yang merujuk pada proses memeriksa jumlah uang yang harus dibayarkan oleh seseorang atas layanan atau produk yang telah diberikan oleh pihak lain. Biasanya, tagihan ini berisi rincian mengenai jenis layanan atau produk yang digunakan, jumlah yang harus dibayar, dan tanggal jatuh tempo pembayaran. Dengan melakukan "cek tagihan", seseorang dapat memastikan bahwa tagihan yang diterima sesuai dengan layanan atau produk yang telah digunakan. Dibuat menggunakan bahasa pemrograman Python3 dan metode scraping. Scraping adalah teknik ekstraksi data yang dilakukan dengan cara mengambil informasi dari sebuah website bukalapak secara otomatis, menggunakan library atau framework tertentu

Project ini dibuat untuk tujuan pengembangan dan pembelajaran



## Library

 - [Requests](https://pypi.org/project/requests/)
 - [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
 - [Requests-toolbelt](https://pypi.org/project/requests-toolbelt/)
 - [Fake_useragent](https://pypi.org/project/fake-useragent/)

## Fitur

| Nama             | Status                                                                |
| ----------------- | ------------------------------------------------------------------ |
| prepaidInquiries ( Token Listrik ) | ✅ |
| postpaidInquiries ( Tagihan Listrik ) | ✅ |
| pdamInquiries ( Tagihan PDAM ) | ✅ |
| bpjsKesehatanInquiries ( Tagihan BPJS ) | ✅ |


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
    {
        'status': True, 
        'customer_number': 'xxxxxx', 
        'customer_name': 'x xxxx xxxxxx', 
        'segmentation': 'R1', 
        'power': 2200
    }
    
    # contoh output jika gagal
     {
         'status': False, 
         'customer_number': '32030522701'
     }
    

