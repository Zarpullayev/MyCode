import os
import platform
import uuid
import socket

# 📌 **1️⃣ Qurilmaning haqiqiy Device ID sini olish**  
def get_device_id():
    system_name = platform.system()  # Windows, Linux, macOS
    node_name = platform.node()  # Qurilma nomi
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xFF) for elements in range(0, 2*6, 8)][::-1])  # MAC Address
    hostname = socket.gethostname()  # Kompyuter nomi
    return f"{system_name}-{node_name}-{mac_address}-{hostname}"  # Yagona Device ID

# Qurilma ID ni olish va ekranga chiqarish
current_device = get_device_id()
print(f"🖥 Qurilma ID: {current_device}")

# 📌 **2️⃣ GitHub Secrets'dan DEVICE_ID ni olish**
allowed_device = os.getenv("DEVICE_ID")

# 📌 **3️⃣ Qurilma ID ni tekshirish**
if allowed_device is None:
    print("❌ Ruxsat yo'q: GitHub Secrets'da DEVICE_ID topilmadi!")
    exit()

if current_device != allowed_device:
    print("❌ Ruxsat yo'q: Noto'g'ri qurilma!")
    exit()

print("✅ Ruxsat berildi! Kod ishga tushmoqda...")

# 📌 **4️⃣ Asosiy kod (Bu yerga sening koding kiradi)**
print("🚀 Asosiy kod ishlayapti...")
