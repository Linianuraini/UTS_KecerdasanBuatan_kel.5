# Aplikasi Penunjuk Jalan Kampus UNIB

Aplikasi pencari rute tercepat antar gedung di lingkungan kampus Universitas Bengkulu (UNIB), menggunakan algoritma **Breadth-First Search (BFS)**. Dilengkapi dengan antarmuka berbasis **Tkinter**, peta interaktif dari **Folium**, serta fitur pengecekan akses jalan berdasarkan **hari dan waktu**.

---

## Fitur Utama

- Menampilkan rute tercepat antar gedung kampus
- Memperhitungkan kondisi akses jalan berdasarkan hari dan jam
- Visualisasi jalur di peta interaktif dengan Folium
- Input pilihan kendaraan, waktu, dan hari
- Antarmuka GUI sederhana dan intuitif dengan Tkinter

---

## Konsep Algoritma: Breadth-First Search (BFS)

**BFS (Breadth-First Search)** adalah algoritma pencarian jalur dalam graf tak berbobot yang mencari rute tercepat berdasarkan **jumlah simpul terkecil**. BFS cocok untuk lingkungan kecil–menengah seperti peta kampus.

### Kelebihan BFS:
- Selalu menemukan jalur dengan langkah paling sedikit
- Cepat dan ringan untuk graf berskala kecil
- Bisa dikombinasikan dengan logika pembatasan akses (hari & jam)

### Kelemahan:
- Kurang efisien untuk wilayah besar
- Tidak mempertimbangkan bobot (waktu tempuh atau jarak)

---

## Studi Kasus: UNIB

### Masalah:
Menemukan jalur tercepat dari satu gedung ke gedung lain, dengan memperhatikan apakah gerbang/jalan tertentu sedang **dibuka atau ditutup**.

### Formulasi:
- **Input:** Graf G = (V, E), titik awal s, titik tujuan t
- **Tujuan:** Temukan path P = (s, ..., t) dengan |P| minimum
- **Kondisi:** Semua edge dalam P boleh dilewati (akses terbuka)

---

## Cara Kerja Aplikasi

1. **Representasi Graf**
   - Setiap gedung = node
   - Jalan antar gedung = edge
   ```python
   graph = {
       'Gedung A': ['Gedung B', 'Gedung C'],
       'Gedung B': ['Gedung A', 'Gedung D'],
       ...
   }
   
readme_content = """
## Langkah Penerapan:

1. **Representasi kampus sebagai graf** = Tiap gedung adalah simpul, jalan sebagai sisi.
2. **Menentukan node awal dan tujuan** = Input dari pengguna (misalnya: Gedung 5 ke Dekanat Teknik).
3. **Algoritma BFS mencari jalur tercepat (simpul terkecil)** = Fungsi `bfs_shortest_path(graph, start, goal)` berjalan.
4. **Memfilter akses jika gerbang tidak buka** = Dicek menggunakan fungsi `get_accessible_edges(day, ur)`.
5. **Visualisasi jalur pada peta** = Menggunakan **Folium**. `PolyLine()` dan `folium.Marker()` digunakan untuk menampilkan jalur di peta.

## 1. Seberapa Cepat Algoritmanya Bekerja?
Secara teori, kecepatan BFS itu tergantung dari:
- **V**: jumlah titik (misalnya gedung, taman, gerbang, dll)
- **E**: jumlah jalur yang menghubungkan titik-titik tadi

Waktu komputasi BFS itu sekitar **O(V + E)**. Artinya, makin banyak titik dan jalur, makin banyak yang diproses. Tapi karena peta kampus nggak terlalu besar, prosesnya tetap cepat dan ringan.

## 2. Kenapa BFS Cocok Buat Aplikasi Ini?
- **Selalu dapet rute dengan langkah paling sedikit**: BFS ngasih jalur tercepat dalam hal jumlah titik yang dilewati. Jadi kita bisa sampai tujuan tanpa muter-muter terlalu banyak.
- **Pas buat skala kecil**: Kayak kampus UNIB yang punya graf terbatas.
- **Lingkungan terbatas**: BFS sangat cocok buat lingkungan terbatas seperti kampus yang nggak terlalu besar.

## Referensi dan Dasar Teori

- Dari buku **Introduction to Algorithms**: [Link ke Buku](https://books.google.co.id/books?id=NLngYyWFl_YC&printsec=copyright&hl=id#v=onepage&q&f=false)  
  BFS bagus buat nyari jalur tercepat di graf tanpa bobot.

- Dari **The Art of Computer Programming (Donald Knuth)**: [Link ke Buku](https://g.co/kgs/uGCChe8)  
  BFS efisien banget buat struktur jalur yang jelas dan teratur, kayak peta.

---

## Kesimpulannya
BFS adalah pilihan yang tepat buat aplikasi pencari rute di kampus UNIB karena:
- Lingkungan kampus nggak terlalu luas.
- Jika ingin mendapatkan hasil yang lebih baik, algoritma BFS bisa digabungkan dengan algoritma lainnya.

---

## Rekomendasi untuk Meningkatkan Performance:
1. **Butuh efisiensi untuk graf besar**: Gunakan struktur **Priority Queue (heap)**.
2. **Untuk mempertimbangkan waktu tempuh dan kondisi gerbang**: Algoritma **A\* (A-star)** bisa dipadukan.
3. **Caching/memorization**: Jika ingin mencari rute dari titik yang sama, gunakan caching/memorization untuk menyimpan hasil pencarian sebelumnya (misalnya dengan menggunakan **functools.lru_cache** atau **dict manual**).
4. **Algoritma berat**: Pencarian rute sebaiknya dijalankan di **thread terpisah** agar antarmuka pengguna tetap responsif.

   

## Beberapa contoh percobaan pencarian rute
### 1. Rute: Danau Inspirasi ke ATM UNIB
![Screenshot 2025-04-20 225212r](https://github.com/user-attachments/assets/c24af0f2-07ec-4fb7-b45d-26578a1eb05f)
![Screenshot (307)](https://github.com/user-attachments/assets/b89e03b4-b6aa-4ecf-b09c-762c51398ad9)

### 2. Rute: Dekanat FEB ke GB III
![Screenshot 2025-04-20 234445](https://github.com/user-attachments/assets/d7cf030d-e36b-42b5-be6c-d29430962a32)
![Screenshot (351)](https://github.com/user-attachments/assets/9ba33628-e3be-4336-8d0e-5246018993ce)

### 3. Rute: Gedung V ke Dekanat Teknik
![Screenshot 2025-04-20 233334](https://github.com/user-attachments/assets/03c28b06-8f40-4263-8b37-f97a6a3ce996)
![Screenshot (312)](https://github.com/user-attachments/assets/8acbdb7d-994b-44c9-bcf9-6f3e5f6a3d57)

### 4. Rute: Dekanat FKIK ke GB V
![Screenshot 2025-04-20 235339](https://github.com/user-attachments/assets/f3a38ac2-fcc2-4681-8a90-c24a8a0995d4)
![Screenshot (352)](https://github.com/user-attachments/assets/e5034d24-d3c9-48b3-9cc3-db675f28e411)

### 5. Rute: GLT ke Dekanat Hukum
![![Screenshot 2025-04-21 000536](https://github.com/user-attachments/assets/f2cb528f-1222-4bec-9267-08ccdb63fecb)
![Screenshot (353)](https://github.com/user-attachments/assets/a3363a6a-ad7a-4cc3-a463-87a2acae4ff2)

### 6. Rute: Dekanat Fisip ke GSG
![Screenshot 2025-04-21 001445](https://github.com/user-attachments/assets/cb63da02-0913-4e24-8859-d8778b8340e2)

### 7. Rute: Dekanat FMIPA ke Dekanat FEB
![Screenshot 2025-04-21 001856](https://github.com/user-attachments/assets/75cff82d-8161-46a6-98ce-0b3c7895f3df)
![Screenshot (354)](https://github.com/user-attachments/assets/1bcebd9c-823c-466d-98fe-b9e22c8655c6)

### 8. Rute: Rektorat ke PKM
![Screenshot 2025-04-21 002523](https://github.com/user-attachments/assets/db9705be-d5ad-4e77-a2ff-c287d1777db5)
![Screenshot (355)](https://github.com/user-attachments/assets/6b78cecb-33fc-48e5-8112-1232cd6dccf4)

### 9. Rute: GB 1 ke  GB IV
![Screenshot 2025-04-21 004324](https://github.com/user-attachments/assets/0e26599f-bbbf-4b6e-8c0a-f244a9b98ef0)
![Screenshot (357)](https://github.com/user-attachments/assets/03b532a8-a897-4eea-ae8d-7c0bd836d0f3)

### 10. Rute: Ged K ke Shelter
![Screenshot 2025-04-21 005913](https://github.com/user-attachments/assets/f29ec358-a87f-4689-afe0-47bb3d128300)
![Screenshot (358)](https://github.com/user-attachments/assets/8ee7aa27-8332-4759-a062-33376ed92ba5)

### 11. Rute: Lab Agro ke Lab Teknik Terpadu
![Screenshot 2025-04-21 011004](https://github.com/user-attachments/assets/2565c51b-7f33-44d8-892e-057a9aff0ee1)
![Screenshot (359)](https://github.com/user-attachments/assets/2512f03d-3992-4eec-898d-60849a04fa27)

### 12. Rute: Dekanat FEB ke Perpustakaan
![Screenshot 2025-04-21 011515](https://github.com/user-attachments/assets/66dc8a9d-eac8-460f-8668-c318861ec4fb)
![Screenshot (360)](https://github.com/user-attachments/assets/97c2a69b-308c-45da-878f-b51a598d7a99)

### 13. Rute: Gerbang masuk rektorat ke Shelter
![Screenshot 2025-04-21 081748](https://github.com/user-attachments/assets/8d5e71d2-ce87-4eaa-940a-de8ebfe7f58e)
![Screenshot (361)](https://github.com/user-attachments/assets/2fa350cf-e886-43cf-88a2-4d49537d979d)

### 14. Rute: GB III ke Masjid Baitul Hikmah
![Screenshot 2025-04-21 082530](https://github.com/user-attachments/assets/c586c6e2-921d-4923-a0f2-400d85afae4f)
![Screenshot (362)](https://github.com/user-attachments/assets/2b06d560-c041-4f91-8030-e1c44fbff851)

### 15. Rute: Pasca hukum ke GLT
![![Screenshot 2025-04-21 083457](https://github.com/user-attachments/assets/3ef0ab8b-7944-41a2-b92b-250200b244f9)
![Screenshot (363)](https://github.com/user-attachments/assets/a0242192-7e46-49fb-9b72-553a958a3e09)


gambar diatas merupakan beberapa contoh pencarian rute pada peta unib langkah pertama yang dilakukan yaitu menginputkan lokasi awal, lokasi tujuan, kendaraan, hari dan waktu. terdapat hari dan waktu disini karena berfungsi untuk menentukan apakah rute tersedia atau tidak.
