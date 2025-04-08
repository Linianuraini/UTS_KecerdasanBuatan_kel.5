import tkinter as tk
from tkinter import ttk, messagebox
import datetime

# Definisi Graf dengan Bobot dan Kendaraan (Waktu Tempuh dalam Menit dan Jarak dalam Meter)
graph = {
    "Gerbang masuk UNIB belakang": [("Dekanat Teknik", 3, 200)],
    "Gerbang keluar UNIB belakang": [("Ruang seminar LTE", 3, 200)],
    "Ruang seminar LTE": [("Gerbang keluar UNIB belakang", 3, 200), ("Lab terpadu Teknik", 4, 250), ("Pusat kegiatan mahasiswa Teknik", 5, 300)],
    "Lab terpadu Teknik": [("Ruang seminar LTE", 4, 250), ("Dekanat Teknik", 3, 200)],
    "Pusat kegiatan mahasiswa Teknik": [("Ruang seminar LTE", 5, 300), ("Stadion", 4, 250)],
    "Dekanat Teknik": [("Lab terpadu Teknik", 3, 200), ("Gerbang masuk UNIB belakang", 3, 200), ("LPTIK", 5, 300), ("GSG", 4, 250)],
    "LPTIK": [("Dekanat Teknik", 5, 300), ("Masjid Baitul Hikmah", 3, 200)],
    "Masjid Baitul Hikmah": [("LPTIK", 3, 200), ("GB II", 4, 250)],
    "GSG": [("Dekanat Teknik", 4, 250), ("GB III", 3, 200), ("Dekanat FKIP", 6, 350)],
    "Dekanat FKIP": [("GSG", 6, 350), ("GB II", 3, 200)],
    "GB III": [("GSG", 3, 200), ("Stadion", 5, 300), ("GB IV", 3, 200)],
    "GB IV": [("GB III", 3, 200), ("GB V", 3, 200)],
    "GB V": [("GB IV", 3, 200), ("PSPD", 5, 300), ("PKM", 4, 250)],
    "PSPD": [("GB V", 5, 300), ("Stadion", 6, 350)],
    "Stadion": [("PSPD", 6, 350), ("GB III", 5, 300), ("Pusat kegiatan mahasiswa Teknik", 4, 250)],
    "GB II": [("Masjid Baitul Hikmah", 4, 250), ("GB I", 4, 250), ("Dekanat FKIP", 3, 200), ("Dekanat FISIP", 4, 250)],
    "GB I": [("GB II", 4, 250), ("Shelter", 3, 200), ("Lab. ranper", 5, 300), ("Perpustakaan", 4, 250)],
    "Shelter": [("GB I", 3, 200), ("Danau Inspirasi", 3, 200)],
    "Danau Inspirasi": [("Shelter", 3, 200), ("REKTORAT", 4, 250)],
    "Perpustakaan": [("GB I", 4, 250), ("PKM", 3, 200)],
    "PKM": [("Perpustakaan", 3, 200), ("GB V", 4, 250), ("Dekanat FMIPA", 5, 300)],
    "Dekanat FMIPA": [("PKM", 5, 300), ("Lab. Agro", 4, 250)],
    "Lab. Agro": [("Dekanat FMIPA", 4, 250), ("Ged. Basic Sains", 6, 350)],
    "Ged. Basic Sains": [("Lab. Agro", 6, 350), ("Lab. ranper", 5, 300), ("GKB I", 3, 200)],
    "Lab. ranper": [("Ged. Basic Sains", 5, 300), ("GB I", 5, 300), ("Ged. V", 4, 250)],
    "Ged. V": [("Lab. ranper", 4, 250), ("Ged. T", 3, 200), ("GLT", 4, 250)],
    "GLT": [("Ged. V", 4, 250), ("Ged. I", 5, 300)],
    "Ged. T": [("Ged. V", 3, 200), ("Dekanat Pertanian", 4, 250)],
    "Dekanat Pertanian": [("Ged. T", 4, 250), ("MAKSI (Ged. C)", 6, 350)],
    "MAKSI (Ged. C)": [("Dekanat Pertanian", 6, 350), ("Ged. B", 4, 250), ("Pasca hukum", 4, 250)],
    "Ged. F": [("Pasca hukum", 4, 250), ("Ger UNIB", 3, 200)],
    "Ger UNIB": [("Ged. F", 3, 200), ("CIP Market", 4, 250)],
    "CIP Market": [("Ger UNIB", 4, 250)],
    "Masjid Darul Ulum": [("Ged. A", 3, 200)],
    "Ged. A": [("Masjid Darul Ulum", 3, 200), ("Ged. B", 5, 300)],
    "Ged. B": [("Ged. A", 5, 300), ("MAKSI (Ged. C)", 4, 250)],
    "Ged. I": [("GLT", 5, 300), ("Ged. J", 3, 200)],
    "Ged. J": [("Ged. I", 3, 200), ("ATM UNIB", 3, 200), ("Ged. R UPT B. Inggris", 4, 250)],
    "ATM UNIB": [("Ged. J", 3, 200), ("REKTORAT", 3, 200), ("Klinik UNIB", 3, 200)],
    "REKTORAT": [("ATM UNIB", 3, 200), ("Danau Inspirasi", 4, 250), ("Dekanat FISIP", 4, 250), ("Gerbang masuk rektorat", 2, 150)],
    "Gerbang masuk rektorat": [("REKTORAT", 2, 150)],
    "Klinik UNIB": [("ATM UNIB", 3, 200), ("BNI UNIB", 3, 200)],
    "BNI UNIB": [("Klinik UNIB", 3, 200), ("Ged. MPP", 3, 200)],
    "Ged. MPP": [("BNI UNIB", 3, 200), ("Ged. MM", 4, 250)],
    "Ged. MM": [("Ged. MPP", 4, 250), ("Ged. K", 3, 200)],
    "Ged. K": [("Ged. MM", 3, 200), ("Dekanat FEB", 3, 200)],
    "Dekanat FEB": [("Ged. K", 3, 200), ("Dekanat Hukum", 4, 250)],
    "Dekanat Hukum": [("Dekanat FEB", 4, 250), ("Pasca hukum", 4, 250)],
    "Ged. R UPT B. Inggris": [("Ged. J", 4, 250), ("Pasca hukum", 5, 300)],
    "Pasca hukum": [("Ged. R UPT B. Inggris", 5, 300), ("Dekanat Hukum", 4, 250), ("MAKSI (Ged. C)", 4, 250), ("Ged. F", 6, 350)],
    "Dekanat FISIP": [("REKTORAT", 4, 250), ("GB II", 4, 250)],
    "GKB I": [("Ged. Basic Sains", 3, 200)]
}

# Kecepatan Rata-rata Kendaraan (km/jam) - Tidak Digunakan Langsung
transport_speed = {
    "Motor": 30,
    "Mobil": 20,
    "Sepeda": 10,
    "Jalan Kaki": 5
}

def bfs_shortest_path(graph, start, goal, day):
    """Mencari jalur terpendek dengan BFS."""
    explored = []
    queue = [[start]]

    if start == goal:
        return [start], 0, 0

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbors = []
            for neighbor, time, distance in graph[node]:
                neighbors.append((neighbor, time, distance))

            # Adjust neighbors based on the day
            if day in ["Sabtu", "Minggu"] and node == "Gerbang masuk UNIB belakang":
                neighbors = neighbors[:1]  # Hanya satu jalur dibuka

            for neighbor, time, distance in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == goal:
                    total_time = 0
                    total_distance = 0
                    for i in range(len(new_path) - 1):
                        current = new_path[i]
                        next_node = new_path[i + 1]
                        for n, t, d in graph[current]:
                            if n == next_node:
                                total_time += t
                                total_distance += d
                                break
                    return new_path, total_time, total_distance

            explored.append(node)

    return None, "Tidak ada jalur dari {} ke {}".format(start, goal), 0

def find_path():
    start_node = start_combobox.get()
    goal_node = goal_combobox.get()
    selected_vehicle = vehicle_combobox.get()
    selected_day = day_combobox.get()

    if not start_node or not goal_node or not selected_vehicle or not selected_day:
        messagebox.showerror("Error", "Silakan pilih semua opsi.")
        return

    selected_time = time_combobox.get()
    hour = int(selected_time.split(":")[0])

    if hour < 6 or hour >= 22:
        result_label.config(text="Tidak dapat mencari rute karena gerbang tutup.")
        return

    if start_node not in graph or goal_node not in graph:
        messagebox.showerror("Error", "Titik awal atau tujuan tidak ditemukan dalam graf.")
        return

    path, total_time, total_distance = bfs_shortest_path(graph, start_node, goal_node, selected_day)

    if isinstance(path, list):
        result_label.config(text=f"Jalur: {' -> '.join(path)}\n"
                                   f"Waktu Tempuh ({selected_vehicle}): {total_time} menit\n"
                                   f"Jarak: {total_distance} meter")
    else:
        result_label.config(text=total_time)

def reset_search():
    start_combobox.set('')
    goal_combobox.set('')
    vehicle_combobox.set('')
    day_combobox.set('')
    time_combobox.set('')
    result_label.config(text="")

# GUI Setup
root = tk.Tk()
root.title("Pencarian Rute UNIB")
root.geometry("580x550")
root.configure(bg="#ffb6c1")  # Warna Pink

# Style
style = ttk.Style()
style.configure("TLabel", background="#ffb6c1", font=("Arial", 11), foreground="#880e4f")  # Pink Tua
style.configure("TCombobox", padding=5, font=("Arial", 11))
style.configure("TButton", padding=5, font=("Arial", 11))

# Input Frame
input_frame = tk.Frame(root, bg="#ffb6c1")
input_frame.pack(pady=10)

label_padding = {'padx': 10, 'pady': 5}
combobox_width = 28

# Labels and Combo Boxes
tk.Label(input_frame, text="Lokasi Awal:", font=("Arial", 11), foreground="#880e4f").grid(row=0, column=0, sticky="w", **label_padding)
start_combobox = ttk.Combobox(input_frame, values=sorted(list(graph.keys())), state="readonly", width=combobox_width, style="TCombobox")
start_combobox.grid(row=0, column=1, **label_padding)

tk.Label(input_frame, text="Lokasi Tujuan:", font=("Arial", 11), foreground="#880e4f").grid(row=1, column=0, sticky="w", **label_padding)
goal_combobox = ttk.Combobox(input_frame, values=sorted(list(graph.keys())), state="readonly", width=combobox_width, style="TCombobox")
goal_combobox.grid(row=1, column=1, **label_padding)

tk.Label(input_frame, text="Kendaraan:", font=("Arial", 11), foreground="#880e4f").grid(row=2, column=0, sticky="w", **label_padding)
vehicle_combobox = ttk.Combobox(input_frame, values=["Motor", "Mobil", "Sepeda", "Jalan Kaki"], state="readonly", width=combobox_width, style="TCombobox")  # Pilihan Kendaraan
vehicle_combobox.grid(row=2, column=1, **label_padding)

tk.Label(input_frame, text="Hari:", font=("Arial", 11), foreground="#880e4f").grid(row=3, column=0, sticky="w", **label_padding)
day_combobox = ttk.Combobox(input_frame, values=["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"], state="readonly", width=combobox_width, style="TCombobox")
day_combobox.grid(row=3, column=1, **label_padding)

tk.Label(input_frame, text="Waktu (00:00-24:00):", font=("Arial", 11), foreground="#880e4f").grid(row=4, column=0, sticky="w", **label_padding)
time_values = [f"{i:02d}:00" for i in range(24)]
time_combobox = ttk.Combobox(input_frame, values=time_values, state="readonly", width=combobox_width, style="TCombobox")
time_combobox.grid(row=4, column=1, **label_padding)

# Buttons Frame
button_frame = tk.Frame(root, bg="#ffb6c1")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Cari Rute", command=find_path, bg="#2196F3", fg="white", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)  # Biru
tk.Button(button_frame, text="Reset", command=reset_search, bg="#f44336", fg="white", font=("Arial", 11)).pack(side=tk.LEFT, padx=5)  # Merah

# Result Label
result_label = tk.Label(root, text="", wraplength=550, justify="left", font=("Arial", 11), bg="#ffb6c1", foreground="#880e4f")
result_label.pack(pady=10)

# Note Label
note_label = tk.Label(root, text="Catatan: Waktu tempuh dan jarak adalah perkiraan dan dapat bervariasi.", font=("Arial", 9), bg="#ffb6c1", foreground="#880e4f")
note_label.pack()

root.mainloop()
