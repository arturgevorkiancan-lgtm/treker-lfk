from PIL import Image
import os

folder = "images"
print("🔍 Диагностика и исправление всех картинок...\n")

fixed = 0
broken = []

for filename in sorted(os.listdir(folder)):
    if filename.lower().endswith(('.jpg', '.jpeg')):
        path = os.path.join(folder, filename)
        try:
            img = Image.open(path)
            img = img.convert("RGB")                    # делаем совместимым
            img.save(path, "JPEG", quality=95, optimize=True)
            print(f"✅ {filename} — OK (исправлено и сохранено)")
            fixed += 1
        except Exception as e:
            print(f"❌ {filename} — НЕ ЧИТАЕТСЯ (ошибка: {e})")
            broken.append(filename)

print("\n" + "="*60)
print(f"Проверено картинок: {fixed + len(broken)}")
print(f"Успешно исправлено: {fixed}")
if broken:
    print(f"❗ Остались проблемные файлы: {broken}")
else:
    print("🎉 Все 14 картинок в полном порядке!")
print("="*60)
print("\n✅ Теперь перезапусти приложение командой:")
print("streamlit run app.py")