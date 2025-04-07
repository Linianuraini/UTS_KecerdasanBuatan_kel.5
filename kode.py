from collections import deque
from datetime import datetime, time

def is_time_valid(time_str):
    """Memeriksa apakah waktu berada dalam rentang 06:00 - 22:00"""
    try:
        input_time = datetime.strptime(time_str, "%H:%M").time()
        start_time = time(6, 0)
        end_time = time(22, 0)
        return start_time <= input_time <= end_time
    except ValueError:
        return False

def bfs_shortest_path(graph, start, end, day, time_str, transport_mode):
    """
    Mencari jalur terpendek menggunakan algoritma BFS dengan mempertimbangkan:
    - Hari (weekend/weekday)
    - Waktu (jam gerbang buka/tutup)
    - Moda transportasi (motor, sepeda, jalan kaki)
    """
    # Normalisasi input
    start = start.strip()
    end = end.strip()
    day_lower = day.lower()
    
    # Cek apakah lokasi ada dalam graph
    if start not in graph:
        return f"Lokasi awal '{start}' tidak ditemukan pada peta."
    if end not in graph:
        return f"Lokasi tujuan '{end}' tidak ditemukan pada peta."
    
    # Validasi waktu
    if not is_time_valid(time_str):
        return "Tidak dapat menemukan rute karena gerbang sudah tutup (di luar jam 06:00 - 22:00)."
    
    # Cek batasan gerbang
    weekend_days = ["sabtu", "minggu", "saturday", "sunday"]
    
    # Parse waktu
    try:
        hour, minute = map(int, time_str.split(':'))
        current_time = time(hour, minute)
    except (ValueError, TypeError):
        return "Format waktu tidak valid. Gunakan format 24 jam (HH:MM)."
    
    # Cek apakah gerbang rektorat ditutup pada akhir pekan
    if day_lower in weekend_days and start == "Gerbang masuk rektorat":
        return "Gerbang masuk rektorat ditutup pada hari Sabtu dan Minggu."
    
    # Cek apakah gerbang ditutup setelah jam 10 malam
    closing_time = time(22, 0)  # 10 PM
    gates = ["Gerbang depan", "Gerbang masuk rektorat", "Gerbang keluar UNIB belakang", "Gerbang masuk UNIB belakang"]
    if start in gates and current_time >= closing_time:
        return "Semua gerbang ditutup setelah jam 10 malam."
    
    # Area yang dibatasi berdasarkan moda transportasi
    restricted_areas = {
        "motor": ["Perpustakaan", "Stadion"],  # Area di mana motor tidak diizinkan
        "sepeda": [],  # Tidak ada batasan untuk sepeda
        "jalan kaki": []  # Tidak ada batasan untuk pejalan kaki
    }
    
    # Inisialisasi struktur data untuk BFS
    queue = deque([(start, [start])])
    visited = set([start])
    
    while queue:
        current, path = queue.popleft()
        
        # Jika sudah mencapai tujuan, kembalikan jalur
        if current == end:
            return path
        
        # Tambahkan tetangga ke antrian
        for neighbor in graph[current]:
            # Lewati jika tetangga adalah gerbang dengan batasan
            if neighbor in gates:
                # Lewati gerbang setelah jam tutup
                if current_time >= closing_time:
                    continue
                # Lewati gerbang rektorat pada akhir pekan
                if neighbor == "Gerbang masuk rektorat" and day_lower in weekend_days:
                    continue
            
            # Lewati jika tetangga dibatasi berdasarkan moda transportasi
            if neighbor in restricted_areas.get(transport_mode, []):
                continue
                
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    # Jika tidak ada jalur yang ditemukan
    return f"Tidak ada rute yang tersedia dari {start} ke {end} menggunakan {transport_mode}."

def create_map_graph():
    """Membuat representasi peta UNIB berdasarkan gambar"""
    return {
        # Gerbang utama
        "Gerbang depan": ["Ged. A", "Ged. B"],
        "Gerbang masuk rektorat": ["Rektorat"],
        "Gerbang keluar UNIB belakang": ["Dekanat teknik", "Lab terpadu Teknik"],
        "Gerbang masuk UNIB belakang": ["Dekanat teknik", "Lab terpadu Teknik"],
        
        # Area utama
        "Masjid Darul Ulum": ["Ged. A"],
        "Ged. A": ["Gerbang depan", "Masjid Darul Ulum", "Ged. B"],
        "Ged. B": ["Gerbang depan", "Ged. A", "MAKSI (Ged. C)"],
        "MAKSI (Ged. C)": ["Ged. B", "Pasca hukum"],
        "Pasca hukum": ["MAKSI (Ged. C)", "Ged. F"],
        "Ged. F": ["Pasca hukum", "Ged. J"],
        "Ged. J": ["Ged. F", "Ged. I"],
        "Ged. I": ["Ged. J", "Ged. MM"],
        "Ged. MM": ["Ged. I", "Ged. K"],
        "Ged. K": ["Ged. MM", "Dekanat FEB"],
        "Dekanat FEB": ["Ged. K", "Ged. MPP"],
        "Ged. MPP": ["Dekanat FEB", "BNI UNIB"],
        "BNI UNIB": ["Ged. MPP", "Ged. R UPT B. Inggris"],
        "Ged. R UPT B. Inggris": ["BNI UNIB", "Klinik UNIB"],
        
        # Area Rektorat
        "Klinik UNIB": ["Ged. R UPT B. Inggris", "Rektorat"],
        "Rektorat": ["Klinik UNIB", "ATM UNIB", "Gerbang masuk rektorat"],
        "ATM UNIB": ["Rektorat", "Dekanat FISIP"],
        
        # Area Tengah
        "Dekanat FISIP": ["ATM UNIB", "Danau inspirasi"],
        "Danau inspirasi": ["Dekanat FISIP", "Shelter", "GB II"],
        "Shelter": ["Danau inspirasi", "GB I", "Perpustakaan"],
        "GB I": ["Shelter", "Perpustakaan"],
        "GB II": ["Danau inspirasi", "Dekanat PKP"],
        "Perpustakaan": ["Shelter", "GB I", "Dekanat FMIPA"],
        
        # Area FMIPA
        "Dekanat FMIPA": ["Perpustakaan", "Lab. agro", "Lab. ranper"],
        "Lab. agro": ["Dekanat FMIPA", "Ged. basic sains"],
        "Ged. basic sains": ["Lab. agro", "PKM"],
        "Lab. ranper": ["Dekanat FMIPA", "Ged. I"],
        "Ged. I": ["Lab. ranper", "GLT"],
        "GLT": ["Ged. I", "Ged. T"],
        "Ged. T": ["GLT", "Dekanat Pertanian"],
        "Dekanat Pertanian": ["Ged. T"],
        
        # Area PKM
        "PKM": ["Ged. basic sains", "GB III"],
        "GB III": ["PKM", "GB IV"],
        "GB IV": ["GB III", "GB V"],
        "GB V": ["GB IV", "PSPD"],
        "PSPD": ["GB V", "Stadion"],
        
        # Area Stadion
        "Stadion": ["PSPD", "Dekanat PKP"],
        "Dekanat PKP": ["Stadion", "GSG", "GB II"],
        "GSG": ["Dekanat PKP", "LPTIK"],
        
        # Area Teknik
        "LPTIK": ["GSG", "Masjid Baitul Hikmah"],
        "Masjid Baitul Hikmah": ["LPTIK", "Dekanat teknik"],
        "Dekanat teknik": ["Masjid Baitul Hikmah", "Pusat kegiatan mahasiswa Teknik", 
                          "Gerbang keluar UNIB belakang", "Gerbang masuk UNIB belakang"],
        "Pusat kegiatan mahasiswa Teknik": ["Dekanat teknik", "Ruang seminar LTE"],
        "Ruang seminar LTE": ["Pusat kegiatan mahasiswa Teknik", "Lab terpadu Teknik"],
        "Lab terpadu Teknik": ["Ruang seminar LTE", "Gerbang keluar UNIB belakang", "Gerbang masuk UNIB belakang"]
    }

def display_locations(graph):
    """Menampilkan semua lokasi yang tersedia dalam peta"""
    print("\nLokasi yang tersedia:")
    locations = sorted(graph.keys())
    cols = 3  # Jumlah kolom untuk tampilan
    for i in range(0, len(locations), cols):
        row = locations[i:i+cols]
        formatted_row = "  ".join(f"{loc}" for loc in row)
        print(formatted_row)

def main():
    """Fungsi utama untuk mencari jalur terpendek di UNIB"""
    print("=== Pencari Rute Terpendek Universitas Bengkulu ===")
    
    # Buat representasi peta
    graph = create_map_graph()
    
    # Tampilkan lokasi yang tersedia
    display_locations(graph)
    
    # Ambil input pengguna
    start_location = input("\nLokasi awal: ")
    end_location = input("Lokasi tujuan: ")
    day = input("Hari (contoh: Senin, Selasa, dll): ")
    time_str = input("Waktu (format 24 jam, contoh: 08:30): ")
    
    # Pilihan moda transportasi
    print("\nPilih moda transportasi:")
    print("1. Motor")
    print("2. Sepeda")
    print("3. Jalan kaki")
    mode_choice = input("Pilihan (1/2/3): ")
    
    # Konversi pilihan ke moda transportasi
    transportation_modes = {
        "1": "motor",
        "2": "sepeda",
        "3": "jalan kaki"
    }
    transport_mode = transportation_modes.get(mode_choice, "jalan kaki")
    
    # Cari jalur terpendek
    path = bfs_shortest_path(graph, start_location, end_location, day, time_str, transport_mode)
    
    # Proses dan tampilkan hasil
    if isinstance(path, list):
        print("\nRute terpendek:")
        for i, location in enumerate(path):
            if i < len(path) - 1:
                print(f"{i+1}. {location} → {path[i+1]}")
            else:
                print(f"{i+1}. {location} (Tujuan)")
        
        # Hitung perkiraan waktu berdasarkan moda transportasi
        total_segments = len(path) - 1
        if transport_mode == "motor":
            est_time = total_segments * 2  # 2 menit per segmen untuk motor
        elif transport_mode == "sepeda":
            est_time = total_segments * 4  # 4 menit per segmen untuk sepeda
        else:  # jalan kaki
            est_time = total_segments * 6  # 6 menit per segmen untuk jalan kaki
        
        print(f"\nEstimasi waktu perjalanan dengan {transport_mode}: {est_time} menit")
        print(f"Jumlah lokasi yang dilalui: {len(path)}")
    else:
        # Jika path adalah string, itu adalah pesan kesalahan
        print("\n" + path)

# Jalankan program
if __name__ == "__main__":
    main()
