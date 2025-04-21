import tkinter as tk
from tkinter import ttk, messagebox
import openrouteservice
import folium
from folium import plugins
import webbrowser

# === GRAF ===
graph = {
    "Gerbang masuk UNIB belakang": [("Dekanat Teknik", 3, 200)],
    "Gerbang keluar UNIB belakang": [("Ruang seminar LTE", 3, 200)],
    "Ruang seminar 1 TE": [("Gerbang keluar UNIB belakang", 3, 200), ("Lab terpadu Teknik", 4, 250), ("Pusat kegiatan mahasiswa Teknik", 5, 300)],
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
    "Dekanat FKIK": [("GB V", 5, 300), ("Stadion", 6, 350)],
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
    "Lab. ranper": [("Ged. Basic Sains", 5, 300), ("GB I", 5, 300),],
    "GLT": [("Ged. V", 4, 250), ("Ged. I", 5, 300)],
    "Dekanat Pertanian": [("Ged. T", 4, 250), ("MAKSI (Ged. C)", 6, 350)],
    "MAKSI (Ged. C)": [("Dekanat Pertanian", 6, 350), ("Ged. B", 4, 250), ("Pasca hukum", 4, 250)],
    "Ged. F": [("Pasca hukum", 4, 250), ("Gor UNIB", 3, 200)],
    "Gor UNIB": [("Ged. F", 3, 200), ("CIP Market", 4, 250)],
    "CIP Market": [("Gor UNIB", 4, 250)],
    "Masjid Darul Ulum": [("Ged. A", 3, 200)],
    "Ged. A": [("Masjid Darul Ulum", 3, 200), ("Ged. B", 5, 300)],
    "Ged. I": [("GLT", 5, 300), ("Ged. J", 3, 200)],
    "Ged. J": [("Ged. I", 3, 200), ("ATM UNIB", 3, 200), ("Ged. R UPT B. Inggris", 4, 250)],
    "ATM UNIB": [("Ged. J", 3, 200), ("REKTORAT", 3, 200), ("Klinik UNIB", 3, 200)],
    "REKTORAT": [("ATM UNIB", 3, 200), ("Danau Inspirasi", 4, 250), ("Dekanat FISIP", 4, 250), ("Gerbang masuk rektorat", 2, 150)],
    "Gerbang masuk rektorat": [("REKTORAT", 2, 150)],
    "Klinik UNIB": [("ATM UNIB", 3, 200), ("BNI UNIB", 3, 200)],
    "BNI UNIB": [("Klinik UNIB", 3, 200), ("Ged. MPP", 3, 200)],
    "Ged. MPP": [("BNI UNIB", 3, 200), ("Ged. MM", 4, 250)],
    "Ged. K": [("Ged. MM", 3, 200), ("Dekanat FEB", 3, 200)],
    "Dekanat FEB": [("Ged. K", 3, 200), ("Dekanat Hukum", 4, 250)],
    "Dekanat Hukum": [("Dekanat FEB", 4, 250), ("Pasca hukum", 4, 250)],
    "Ged. R UPT B. Inggris": [("Ged. J", 4, 250), ("Pasca hukum", 5, 300)],
    "Pasca hukum": [("Ged. R UPT B. Inggris", 5, 300), ("Dekanat Hukum", 4, 250), ("MAKSI (Ged. C)", 4, 250), ("Ged. F", 6, 350)],
    "Dekanat FISIP": [("REKTORAT", 4, 250), ("GB II", 4, 250)],
}

# === KECEPATAN ===
transport_speed = {
    "Motor": 30,
    "Mobil": 20,
    "Sepeda": 10,
    "Jalan Kaki": 5
}

# === KOORDINAT ===
def get_coordinates(location):
    coordinates = {
        "LPTIK": [-3.7585399120952174, 102.27501384731698],
        "Lab FKIP UNIB": [-3.758392040501512, 102.275774557561],
        "Masjid Baitul Hikmah": [-3.7591111062367646, 102.27596315356854],
        "Gerbang masuk UNIB belakang kiri": [-3.759528063195318, 102.27509206349377],
        "Gerbang masuk UNIB belakang kanan": [-3.7594959459514725, 102.27516984754958],
        "Gerbang keluar UNIB belakang": [-3.7593833413845297, 102.27622153665969],
        "Laboratorium Teknik": [-3.758900248419332, 102.27687813799439],
        "Lab terpadu Teknik": [-3.7585449060947007, 102.27737613300471],
        "Dekanat Teknik": [-3.7584853553039843, 102.27670222798585],
        "Pusat kegiatan mahasiswa Teknik": [-3.758244026686112, 102.27733637029671],
        "Ruang seminar 1 TE": [-3.758395914692754, 102.27743292981296],
        "GSG": [-3.757699389491203, 102.27658582536203],
        "Dekanat FKIP": [-3.756395177472117, 102.2774862191239],
        "GB III": [-3.7565491980928214, 102.27652042148364],
        "GB IV": [-3.756145397656578, 102.27642116285875],
        "GB V": [-3.755456383580115, 102.27651767463036],
        "Dekanat FKIK": [-3.755242480945984, 102.27801538873103],
        "Stadion": [-3.7577248967347248, 102.27758972656433],
        "GB II": [-3.7580560505510805, 102.27393748543233],
        "GB I": [-3.7569766686837696, 102.27375530316948],
        "Shelter": [-3.7577338371102247, 102.27359540511276],
        "Danau Inspirasi": [-3.7587160013463103, 102.27337947794777],
        "Perpustakaan": [-3.7568284094044437, 102.2748023990714],
        "PKM": [-3.7564775697093986, 102.27580849385731],
        "Dekanat FMIPA": [-3.756056985256464, 102.27470747192069],
        "Lab. Agro": [-3.757035900353202, 102.2727119033043],
        "Ged. Basic Sains": [-3.7564143157261713, 102.27377543241296],
        "Ged. V": [-3.7578186647453995, 102.27190229895915],
        "GLT": [-3.7581289959410795, 102.27190335322092],
        "Dekanat Pertanian": [-3.758014621797453, 102.27254856573315],
        "MAKSI (Ged. C)": [-3.7591257001427874, 102.2679436237409],
        "Gor UNIB": [-3.7607484023371405, 102.26752305415387],
        "CIP Market": [-3.7615171427453564, 102.271767957989],
        "Masjid Darul Ulum": [-3.757437022319187, 102.26761214880817],
        "Ged. A": [-3.7580303175259866, 102.26774676124411],
        "Ged. I": [-3.760031335452444, 102.27004295811417],
        "Ged. J": [-3.7603431176632367, 102.26978963903959],
        "ATM UNIB": [-3.7601453532972564, 102.27180821079662],
        "REKTORAT": [-3.7595163504559976, 102.27240127630482],
        "Gerbang masuk rektorat": [-3.760624615365814, 102.27266354088177],
        "Klinik UNIB": [-3.7614600870378045, 102.27176432741336],
        "BNI UNIB": [-3.7616823042584304, 102.27169316397679],
        "Ged. LPMPP": [-3.758670931063062, 102.26781463954434],
        "Ged. K": [-3.7611577467276542, 102.26993938382489],
        "Dekanat FEB": [-3.761743377190304, 102.26858922532001],
        "Dekanat Hukum": [-3.760620818963268, 102.26836733434781],
        "Ged. R UPT B. Inggris": [-3.7607652261740827, 102.27035918888033],
        "Pasca hukum": [-3.759545616741641, 102.26814246216549],
        "Dekanat FISIP": [-3.7592163403558247, 102.27445916943643]
    }
    return coordinates.get(location, [-3.7598, 102.2715])  # Default fallback

# === BFS ===
def bfs_shortest_path(graph, start, goal, day):
    explored = []
    queue = [[start]]

    if start == goal:
        return [start], 0, 0

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in explored:
            neighbors = []
            for neighbor, time, distance in graph.get(node, []):
                neighbors.append((neighbor, time, distance))

            if day in ["Sabtu", "Minggu"] and node == "Gerbang masuk UNIB belakang":
                neighbors = neighbors[:1]  # Sabtu/Minggu: hanya jalur khusus

            for neighbor, time, distance in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == goal:
                    total_time = 0
                    total_distance = 0
                    for i in range(len(new_path) - 1):
                        curr = new_path[i]
                        nxt = new_path[i + 1]
                        for n, t, d in graph[curr]:
                            if n == nxt:
                                total_time += t
                                total_distance += d
                                break
                    return new_path, total_time, total_distance

            explored.append(node)

    return None, f"Tidak ada jalur dari {start} ke {goal}.", 0

# Initialize OpenRouteService client with your API key
client = openrouteservice.Client(key='5b3ce3597851110001cf6248e69f2ddf27ab4d8580aa360f540219d9')

# === SHOW MAP ===
def show_map(path, vehicle, time_str, waktu_tempuh, jarak, day):
    if not path:
        return

    mid_index = len(path) // 2
    map_center = get_coordinates(path[mid_index])
    map = folium.Map(location=map_center, zoom_start=17)

    # Load Font Awesome icons and style them
    route_details = f"""
    <div style="background-color: #ffffff; border-radius: 12px; padding: 20px; box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.1); width: 400px; font-family: 'Arial', sans-serif; font-size: 14px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <h3 style="color: #2980b9; font-size: 20px; font-weight: 700;">UNIB Navigator</h3>
            <div style="display: flex; align-items: center;">
                <i class="fa fa-clock" style="color: #e74c3c; font-size: 20px; margin-right: 10px;"></i>
                <span style="color: #e74c3c; font-weight: 600; margin-right: 15px;">{time_str}</span>
                <i class="fa fa-calendar" style="color: #FE4F2D; font-size: 20px; margin-right: 10px;"></i>
                <span style="color: #FE4F2D; font-weight: 600;">{day}</span>
            </div>
        </div>
        <div style="border-top: 3px solid #2980b9; padding-top: 12px; padding-bottom: 12px; margin-bottom: 10px;">
            <div style="display: flex; align-items: center; margin-bottom: 8px;">
                <i class="fa fa-map-marker" style="color: green; font-size: 20px; margin-right: 10px;"></i>
                <span style="color: #2c3e50; font-weight: 600;"><strong>Awal:</strong> {path[0]}</span>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 8px;">
                <i class="fa fa-map-marker" style="color: red; font-size: 20px; margin-right: 10px;"></i>
                <span style="color: #2c3e50; font-weight: 600;"><strong>Tujuan:</strong> {path[-1]}</span>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 8px;">
                <i class="fa-solid fa-map-location" style="color: #FFD700; font-size: 20px; margin-right: 10px;"></i>
                <span style="color: #2c3e50;"><strong>Jarak Tempuh:</strong> {jarak} meter</span>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 8px;">
                <i class="fa fa-hourglass-half" style="color: #3498db; font-size: 20px; margin-right: 10px;"></i>
                <span style="color: #2c3e50;"><strong>Waktu Tempuh:</strong> {int(waktu_tempuh)} menit</span>
            </div>
            <div style="display: flex; align-items: center; margin-bottom: 8px;">
                <i class="fa fa-car" style="color: #9b59b6; font-size: 20px; margin-right: 10px;"></i>
                <span style="color: #2c3e50;"><strong>Kendaraan:</strong> {vehicle}</span>
            </div>
        </div>
    </div>
    """

    # Adding Font Awesome CDN to the map HTML
    map.get_root().html.add_child(folium.Element('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">'))

    # Add the route details (positioned on the left side of the map)
    map.get_root().html.add_child(folium.Element(f'<div style="position: absolute; top: 20px; left: 20px; z-index: 9999; padding: 15px;">{route_details}</div>'))

    # Get coordinates for start and destination
    start_coord = get_coordinates(path[0])
    end_coord = get_coordinates(path[-1])

    # Check if coordinates are valid and close to roads
    if start_coord == [-3.7598, 102.2715] or end_coord == [-3.7598, 102.2715]:  # Default fallback coordinates
        print("Coordinates are invalid or out of range!")
        return

    try:
        # Request directions from OpenRouteService API
        routes = client.directions(
            coordinates=[(start_coord[1], start_coord[0]), (end_coord[1], end_coord[0])],  # Coordinates in (lon, lat) format
            profile='driving-car',  # Change to 'cycling-regular' or 'foot-walking' based on the vehicle
            format='geojson'
        )

        # Plot the road-following path on the map
        folium.GeoJson(routes, name='Road Followed Path').add_to(map)

        # Add custom markers for start and destination with hover information
        folium.Marker(
            location=start_coord,
            icon=folium.Icon(color='green'),
            tooltip=f"Start: {path[0]}"  # Tooltip showing "Start" when hovering
        ).add_to(map)

        folium.Marker(
            location=end_coord,
            icon=folium.Icon(color='red'),
            tooltip=f"Destination: {path[-1]}"  # Tooltip showing "Destination" when hovering
        ).add_to(map)

        # Save the map as an HTML file and open it in a browser
        map.save("peta_rute.html")
        webbrowser.open("peta_rute.html")

    except openrouteservice.exceptions.ApiError as e:
        print(f"API Error: {e}")
        print(f"Error details: {e.args}")


# === FIND PATH ===
def find_path():
    start = start_combobox.get()
    end = goal_combobox.get()
    vehicle = vehicle_combobox.get()
    day = day_combobox.get()
    time_str = time_combobox.get()

    if not all([start, end, vehicle, day, time_str]):
        messagebox.showerror("Error", "Silakan lengkapi semua opsi terlebih dahulu.")
        return

    jam = int(time_str.split(":")[0])
    if jam < 6 or jam >= 22:
        result_label.config(text="Gerbang tutup pada jam ini. Rute tidak dapat diakses.")
        return

    if start not in graph or end not in graph:
        messagebox.showerror("Error", "Lokasi tidak ditemukan dalam graf.")
        return

    # Calculate the path, time, and distance
    path, waktu, jarak = bfs_shortest_path(graph, start, end, day)

    if isinstance(path, list):
        kecepatan = transport_speed.get(vehicle, 20)
        waktu_tempuh = (jarak / 1000) / kecepatan * 60
        result_label.config(text=f"Jalur: {' → '.join(path)}\n"
                                 f"Waktu Tempuh ({vehicle}): {int(waktu_tempuh)} menit\n"
                                 f"Jarak: {jarak} meter")
        # Call show_map with the required arguments
        show_map(path, vehicle, time_str, waktu_tempuh, jarak, day)
    else:
        result_label.config(text=waktu)

# === RESET SEARCH ===
def reset_search():
    start_combobox.set('')
    goal_combobox.set('')
    vehicle_combobox.set('')
    day_combobox.set('')
    time_combobox.set('')
    result_label.config(text="")


# === GUI ===
# Function to apply modern button styling
def on_enter(button, color):
    button['bg'] = color  # Change background color on hover
    button['fg'] = 'white'  # Change text color on hover

def on_leave(button, color):
    button['bg'] = color  # Revert to original color when not hovered
    button['fg'] = 'white'  # Revert to original text color when not hovered

# Initialize root window
root = tk.Tk()
root.title("Pencarian Rute UNIB")

# Set window size
window_width = 600
window_height = 600

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position to center the window
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# Set the window geometry (centered)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
root.configure(bg="#fce4ec")  # Soft pink background for a modern feel

# Style Configuration
style = ttk.Style()
style.configure("TLabel", background="#fce4ec", font=("Arial", 12), foreground="#880e4f")
style.configure("TCombobox", padding=8, font=("Arial", 12))
style.configure("TButton", padding=10, font=("Arial", 12), width=15)
style.configure("TFrame", background="#fce4ec")

# Input frame with some padding for better spacing
input_frame = tk.Frame(root, bg="#fce4ec")
input_frame.pack(pady=20)

# Label Padding
label_padding = {'padx': 20, 'pady': 10}
combobox_width = 35

# === INPUT FIELDS ===
tk.Label(input_frame, text="Lokasi Awal:", font=("Arial", 12), bg="#fce4ec").grid(row=0, column=0, sticky="w", **label_padding)
start_combobox = ttk.Combobox(input_frame, values=sorted(graph.keys()), state="readonly", width=combobox_width, font=("Arial", 12))
start_combobox.grid(row=0, column=1, **label_padding)

tk.Label(input_frame, text="Lokasi Tujuan:", font=("Arial", 12), bg="#fce4ec").grid(row=1, column=0, sticky="w", **label_padding)
goal_combobox = ttk.Combobox(input_frame, values=sorted(graph.keys()), state="readonly", width=combobox_width, font=("Arial", 12))
goal_combobox.grid(row=1, column=1, **label_padding)

tk.Label(input_frame, text="Kendaraan:", font=("Arial", 12), bg="#fce4ec").grid(row=2, column=0, sticky="w", **label_padding)
vehicle_combobox = ttk.Combobox(input_frame, values=list(transport_speed.keys()), state="readonly", width=combobox_width, font=("Arial", 12))
vehicle_combobox.grid(row=2, column=1, **label_padding)

tk.Label(input_frame, text="Hari:", font=("Arial", 12), bg="#fce4ec").grid(row=3, column=0, sticky="w", **label_padding)
day_combobox = ttk.Combobox(input_frame, values=["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"], state="readonly", width=combobox_width, font=("Arial", 12))
day_combobox.grid(row=3, column=1, **label_padding)

tk.Label(input_frame, text="Waktu (00:00-23:00):", font=("Arial", 12), bg="#fce4ec").grid(row=4, column=0, sticky="w", **label_padding)
time_combobox = ttk.Combobox(input_frame, values=[f"{i:02d}:00" for i in range(24)], state="readonly", width=combobox_width, font=("Arial", 12))
time_combobox.grid(row=4, column=1, **label_padding)

# === BUTTONS ===
button_frame = tk.Frame(root, bg="#fce4ec")
button_frame.pack(pady=20)

# Modern styled buttons with different colors and hover effect
search_button = tk.Button(button_frame, text="Cari Rute", command=find_path, bg="#2196F3", fg="white", relief="flat", font=("Arial", 12), width=20, height=2)
search_button.pack(side=tk.LEFT, padx=10)
search_button.bind("<Enter>", lambda e: on_enter(search_button, '#1976D2'))  # Hover effect (dark blue)
search_button.bind("<Leave>", lambda e: on_leave(search_button, '#2196F3'))  # Revert to original color

reset_button = tk.Button(button_frame, text="Reset", command=reset_search, bg="#f44336", fg="white", relief="flat", font=("Arial", 12), width=20, height=2)
reset_button.pack(side=tk.LEFT, padx=10)
reset_button.bind("<Enter>", lambda e: on_enter(reset_button, '#d32f2f'))  # Hover effect (darker red)
reset_button.bind("<Leave>", lambda e: on_leave(reset_button, '#f44336'))  # Revert to original color

# === RESULT LABEL ===
result_label = tk.Label(root, text="", wraplength=550, justify="left", font=("Arial", 12), bg="#fce4ec", foreground="#880e4f")
result_label.pack(pady=20)

# === FOOTNOTE ===
note_label = tk.Label(root, text="Catatan: Waktu tempuh & jarak bersifat estimasi.", font=("Arial", 10), bg="#fce4ec", foreground="#880e4f")
note_label.pack(pady=10)

# === RUN ===
root.mainloop()