import os
import base64

# GitHub Secrets'dan DEVICE_ID ni olish
allowed_device = os.getenv("DEVICE_ID")

# Qurilmaning haqiqiy ID sini olish (Buni avtomatlashtirish mumkin)
current_device = "123456789ABC"  # Bu joyga haqiqiy qurilma ID olish kodi qo'shilishi mumkin

# Tekshirish
if allowed_device is None:
    print("❌ Ruxsat yo'q: GitHub Secrets'da DEVICE_ID topilmadi!")
    exit()

if current_device != allowed_device:
    print("❌ Ruxsat yo'q: Noto'g'ri qurilma!")
    exit()

print("✅ Ruxsat berildi! Kod ishga tushmoqda...")

# Shifrlangan kod (Base64 formatida)
encoded_script = "cHJpbnQoIk1hbmJhIGtvZCBzaWZybGFuZ2FuZGlyIik="  # Bu joyga asl shifrlangan kod joylanadi

# Kodni dekod qilish va ishga tushirish
exec(base64.b64decode(encoded_script).decode('utf-8'))
