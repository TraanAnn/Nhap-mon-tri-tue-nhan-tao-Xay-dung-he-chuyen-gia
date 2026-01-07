import tkinter as tk
from tkinter import ttk
import os
import json
from PIL import Image, ImageTk

# ================== TẠO THƯ MỤC ==================
for folder in ["images", "data"]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# ================== LOAD RULES ==================
def load_rules_txt():
    rules = []
    path = os.path.join("data", "quancafe_rules.txt")
    if not os.path.exists(path):
        print("Không tìm thấy file:", path)
        return rules
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if "->" not in line or line.startswith("#"):
                continue
            left, right = line.split("->")
            conditions = [x.strip() for x in left.split("^")]
            result = right.strip()
            rules.append({"conditions": conditions, "result": result})
    return rules

RULES = load_rules_txt()

# ================== LOAD DESCRIPTION JSON ==================
def load_descriptions():
    desc = {}
    for fname in os.listdir("data"):
        if fname.startswith("quancafe_") and fname.endswith(".txt") and fname != "quancafe_rules.txt":
            cafe = fname.replace("quancafe_", "").replace(".txt", "")
            path = os.path.join("data", fname)
            try:
                with open(path, encoding="utf-8") as f:
                    desc[cafe] = json.load(f)
            except Exception as e:
                print("Lỗi đọc JSON:", path, e)
    return desc

DESCRIPTIONS_JSON = load_descriptions()

# ================== MAPPING ==================
MAP = {
    "VỊ TRÍ": {
        "Phường 1": "P1",
        "Phường 3": "P2",
        "Phường 4": "P3",
        "Phường 5": "P4",
        "Phường 8": "P5",
        "Phường 9": "P6",
        "Phường Tân Ngãi": "P7",
        "Phường Tân Hòa": "P8",
        "Phường Tân Hội": "P9",
        "Phường Trường An": "P10",
        "Thị trấn Long Hồ": "P11",
        "Phường Long Châu": "P12"
    },
    "GIÁ": {
        "Dưới 50.000": "G1",
        "Từ 50.000 tới 100.000": "G2",
        "Trên 100.000": "G3"
    },
    "KHÔNG GIAN": {
        "Thoáng mát rộng rãi": "K1",
        "Có hồ bơi": "K2",
        "Có hồ cá Koi": "K3",
        "Có khu vui chơi trẻ em": "K4",
        "Không có khu vui chơi trẻ em": "K5",
        "Cafe đọc sách": "K6",
        "Cafe gia đình": "K7",
        "Cafe thư giãn": "K8",
        "Có view đẹp": "K9",
        "Có sân vườn": "K10",
        "Có phòng máy lạnh": "K11",
        "Có chỗ decor chụp ảnh": "K12"
    },
    "DỊCH VỤ": {
        "Cho mang thú cưng": "D1",
        "Không cho mang thú cưng": "D2",
        "Cho mang đồ ăn ngoài": "D3",
        "Không cho mang đồ ăn ngoài": "D4",
        "Có đồ ăn nhẹ": "D5",
        "Không có đồ ăn nhẹ": "D6",
        "Có món chính": "D7",
        "Không có món chính": "D8",
        "Có tổ chức Acoustics": "D9"
    }
}

# Tên quán tương ứng với mã T1 đến T40
CAFE_NAMES = {
    "T1": "Lai coffee & Tea",
    "T2": "Thóc Cafe",
    "T3": "Brownie Coffe & Dessert",
    "T4": "Up Coffee & Tea",
    "T5": "Quán trà An Nhiên (Deliverse)",
    "T6": "Lan's Coffee",
    "T7": "Café Lê Vy",
    "T8": "Nhà Ga Coffe",
    "T9": "Cafe 9H2O",
    "T10": "Café Lê Vy 2",
    "T11": "Sky cà phê",
    "T12": "Mây chiều Tea & Coffee",
    "T13": "Paris Hotel & Café",
    "T14": "The 1996 Coffee & Tea",
    "T15": "L'amour Coffee",
    "T16": "KIM TEA",
    "T17": "Yolo coffee",
    "T18": "Catimo Coffee",
    "T19": "Robusta Coffee",
    "T20": "Boss Coffee",
    "T21": "Vườn của lá",
    "T22": "The Gỗ Coffee & Tea",
    "T23": "Thư CÀFE",
    "T24": "1985 Coffee & Tea",
    "T25": "Tiệm Cà Phê Đời Đá Vàng",
    "T26": "Thảo mộc",
    "T27": "DIA•MOND coffee & tea",
    "T28": "Central Coffee",
    "T29": "Katfie Coffee & Tea",
    "T30": "Én Coffee and Tea",
    "T31": "An Tea&Coffee",
    "T32": "ấm. Trà & coffee",
    "T33": "BONSAI coffee",
    "T34": "Cafe Gạch",
    "T35": "Nâu Coffee & Tea",
    "T36": "Highlands Coffee Vincom",
    "T37": "Bậc Coffee - Rooftop",
    "T38": "Vườn nhà Ú",
    "T39": "The Seasons Coffee & Tea",
    "T40": "Mộc Viên"
}

# ================== GUI ==================
root = tk.Tk()
root.title("Hệ chuyên gia gợi ý quán cà phê Vĩnh Long")
root.state("zoomed")
root.configure(bg="#ffffff")

# Màn hình chính
main_menu = tk.Frame(root, bg="#ffffff")
main_menu.place(x=0, y=0, relwidth=1, relheight=1)

# 
menu_img_path = os.path.join("images", "manhinhchinh.png")
if os.path.exists(menu_img_path):
    img = Image.open(menu_img_path).resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    menu_bg = ImageTk.PhotoImage(img)
    tk.Label(main_menu, image=menu_bg).place(x=0, y=0, relwidth=1, relheight=1)

def start_system():
    main_menu.place_forget()
    expert_frame.place(x=0, y=0, relwidth=1, relheight=1)

tk.Button(main_menu, text="BẮT ĐẦU", font=("Arial", 20, "bold"), bg="#4CAF50", fg="white", width=20, command=start_system).place(relx=0.5, rely=0.6, anchor="center")
tk.Button(main_menu, text="THOÁT", font=("Arial", 20, "bold"), bg="#F44336", fg="white", width=20, command=root.destroy).place(relx=0.5, rely=0.7, anchor="center")

# Frame hệ chuyên gia
expert_frame = tk.Frame(root, bg="#ffffff")

bg_path = os.path.join("images", "background.png")
if os.path.exists(bg_path):
    bg_img = Image.open(bg_path).resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    bg_photo = ImageTk.PhotoImage(bg_img)
    tk.Label(expert_frame, image=bg_photo).place(x=0, y=0, relwidth=1, relheight=1)

# Bên trái - chọn tiêu chí
left = tk.Frame(expert_frame, bg="#ffffff")
left.place(relx=0.01, rely=0.02, relwidth=0.35, relheight=0.96)

select_frame = tk.LabelFrame(left, text="CHỌN TIÊU CHÍ", font=("Arial", 12, "bold"), bg="#ffffff")
select_frame.pack(fill="x", pady=10)

def combo(parent, label, values):
    tk.Label(parent, text=label, bg="#ffffff", font=("Arial", 10, "bold")).pack(anchor="w", padx=10, pady=5)
    cb = ttk.Combobox(parent, values=[""] + list(values), state="readonly")
    cb.set("")
    cb.pack(fill="x", padx=10, pady=2)
    return cb

cb_vitri = combo(select_frame, "VỊ TRÍ", MAP["VỊ TRÍ"].keys())
cb_gia   = combo(select_frame, "GIÁ", MAP["GIÁ"].keys())
cb_khonggian = combo(select_frame, "KHÔNG GIAN", MAP["KHÔNG GIAN"].keys())
cb_dichvu = combo(select_frame, "DỊCH VỤ", MAP["DỊCH VỤ"].keys())

btn_frame = tk.Frame(select_frame, bg="#ffffff")
btn_frame.pack(pady=15)

tk.Button(btn_frame, text="TÌM KIẾM", width=12, font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="XÓA", width=12, font=("Arial", 10, "bold")).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="QUAY LẠI", width=12, font=("Arial", 10, "bold"),
          command=lambda: [expert_frame.place_forget(), main_menu.place(x=0,y=0,relwidth=1,relheight=1)]).grid(row=0, column=2, padx=10)

# Khu vực hiển thị kết quả
result_frame = tk.LabelFrame(left, text="KẾT QUẢ GỢI Ý", font=("Arial", 12, "bold"), bg="#ffffff")
result_frame.pack(fill="both", expand=True, pady=10)

result_text = tk.Text(result_frame, wrap="word", font=("Arial", 11))
result_text.pack(side="left", fill="both", expand=True)
scroll = tk.Scrollbar(result_frame, command=result_text.yview)
scroll.pack(side="right", fill="y")
result_text.config(yscrollcommand=scroll.set, state="disabled")

# Bên phải - ảnh quán
right = tk.Frame(expert_frame, bg="#ffffff")
right.place(relx=0.45, rely=0.02, relwidth=0.52, relheight=0.96)

img_label = tk.Label(right, bg="#ffffff")
img_label.pack(expand=True)

# ================== HIỂN THỊ ẢNH ==================
def display_image(img_path):
    if os.path.exists(img_path):
        img = Image.open(img_path)
        w = right.winfo_width()
        h = right.winfo_height() - 100
        if w < 50: w = 800
        if h < 50: h = 600
        img_ratio = img.width / img.height
        frame_ratio = w / h
        if img_ratio > frame_ratio:
            new_w = w
            new_h = int(w / img_ratio)
        else:
            new_h = h
            new_w = int(h * img_ratio)
        img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        img_label.config(image=photo)
        img_label.image = photo
        img_label.current_path = img_path
    else:
        img_label.config(image="")
        img_label.current_path = None

# ================== TÌM KIẾM ==================
def find():
    facts = set()
    if cb_vitri.get(): facts.add(MAP["VỊ TRÍ"][cb_vitri.get()])
    if cb_gia.get():   facts.add(MAP["GIÁ"][cb_gia.get()])
    if cb_khonggian.get(): facts.add(MAP["KHÔNG GIAN"][cb_khonggian.get()])
    if cb_dichvu.get(): facts.add(MAP["DỊCH VỤ"][cb_dichvu.get()])

    result_text.config(state="normal")
    result_text.delete(1.0, tk.END)
    img_label.config(image="")

    if len(facts) < 4:
        result_text.insert(tk.END, "⚠️ Vui lòng chọn đủ 4 tiêu chí:\n• Vị trí\n• Giá\n• Không gian\n• Dịch vụ")
        result_text.config(state="disabled")
        return

    matched = [r for r in RULES if set(r["conditions"]).issubset(facts)]
    if not matched:
        result_text.insert(tk.END, "😔 Không tìm thấy quán cà phê nào phù hợp với yêu cầu của bạn.")
        result_text.config(state="disabled")
        return

    # Ưu tiên luật cụ thể nhất
    matched.sort(key=lambda x: len(x["conditions"]), reverse=True)
    best = matched[0]
    best_code = best["result"]  # ví dụ T2
    best_name = CAFE_NAMES.get(best_code, best_code)

    result_text.insert(tk.END, f"🎯 GỢI Ý TỐT NHẤT:\n{best_name}\n\n")

    # Tìm mô tả chi tiết từ file JSON
    descs = DESCRIPTIONS_JSON.get(best_code, [])
    found = False
    for d in descs:
        if set(d["conditions"]) == set(best["conditions"]):
            result_text.insert(tk.END, d["description"] + "\n\n")
            found = True
            break
    if not found:
        result_text.insert(tk.END, f"Luật áp dụng: {' ^ '.join(best['conditions'])} -> {best_code}\n")

    # Các lựa chọn khác
    if len(matched) > 1:
        result_text.insert(tk.END, "\nCác quán khác cũng phù hợp:\n")
        for r in matched[1:]:
            name = CAFE_NAMES.get(r["result"], r["result"])
            result_text.insert(tk.END, f"• {name}\n")

    # Hiển thị ảnh
    img_path = os.path.join("images", best_code + ".jpg")  # ví dụ T2.jpg
    display_image(img_path)

    result_text.config(state="disabled")
    result_text.see(1.0)

def clear():
    for cb in [cb_vitri, cb_gia, cb_khonggian, cb_dichvu]:
        cb.set("")
    result_text.config(state="normal")
    result_text.delete(1.0, tk.END)
    result_text.config(state="disabled")
    img_label.config(image="")

# Gắn lệnh cho nút
for w in btn_frame.winfo_children():
    if w.cget("text") == "TÌM KIẾM":
        w.config(command=find)
    elif w.cget("text") == "XÓA":
        w.config(command=clear)

# Resize ảnh khi thay đổi cửa sổ
def on_resize(event):
    if hasattr(img_label, 'current_path') and img_label.current_path:
        display_image(img_label.current_path)
right.bind("<Configure>", on_resize)
img_label.current_path = None

expert_frame.place_forget()
root.mainloop()