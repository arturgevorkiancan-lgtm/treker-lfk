from PIL import Image
import os

# Путь к нашей картинке
image_path = "images/retraction_chin.jpg"

if os.path.exists(image_path):
    try:
        # Открываем и пересохраняем в чистом формате
        img = Image.open(image_path)
        img = img.convert("RGB")          # делаем совместимым
        img.save(image_path, "JPEG", quality=95, optimize=True)
        print("✅ Картинка retraction_chin.jpg успешно исправлена!")
        print("Теперь можно запускать приложение.")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
else:
    print("❌ Файл images/retraction_chin.jpg не найден")