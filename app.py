import streamlit as st
import json
import os
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="Трекер ЛФК • Май 2026", page_icon="🏋️‍♂️", layout="centered")

# ==================== УПРАЖНЕНИЯ С ВИДЕО ====================
exercises = {
    "warm_up": [
        {"name": "Ретракция подбородка", "file": "retraction_chin.jpg", "video_id": "Aoipu_fl3HA", "sets": "10×5 сек", "desc": "Подбородок слегка втягиваем назад."},
        {"name": "Мягкий наклон головы", "file": "head_tilt.jpg", "video_id": None, "sets": "8–10 в каждую сторону", "desc": "Медленно, без рывков."},
        {"name": "Плечевые круги назад", "file": "shoulder_circles.jpg", "video_id": None, "sets": "10 раз", "desc": "Раскрываем грудной отдел."},
        {"name": "Тазовые наклоны у стены", "file": "pelvic_tilt_standing.jpg", "video_id": None, "sets": "10 раз", "desc": "Поясница прижимается к стене."}
    ],
    "lfk_core": [
        {"name": "Dead Bug (Мёртвый жук)", "file": "dead_bug.jpg", "video_id": "Aoipu_fl3HA", "sets": "3×8–10 на сторону", "desc": "Поясница прижата к полу. Главное упражнение при протрузии L5-S1."},
        {"name": "Тазовый наклон лёжа", "file": "pelvic_tilt_lying.jpg", "video_id": None, "sets": "3×12–15", "desc": "Прижимаем поясницу к полу."},
        {"name": "Ягодичный мостик с подушкой", "file": "glute_bridge_pillow.jpg", "video_id": "A35IxrbqVPM", "sets": "3×12–15", "desc": "Под колени — подушка, сильно сжимаем ягодицы."}
    ],
    "lfk_hips": [
        {"name": "Clamshell (Ракушка)", "file": "clamshell.jpg", "video_id": "vsQugiJgZZE", "sets": "3×12–15 на сторону", "desc": "Стопы вместе, поднимаем верхнее колено."}
    ],
    "lfk_thoracic": [
        {"name": "Открытие грудной клетки", "file": "thoracic_opening.jpg", "video_id": None, "sets": "3×45–60 сек", "desc": "На валике вдоль позвоночника."},
        {"name": "Superman", "file": "superman.jpg", "video_id": None, "sets": "3×10–12", "desc": "Лёжа на животе."},
        {"name": "Bird-Dog", "file": "bird_dog.jpg", "video_id": "-LRjkbEy-qU", "sets": "3×8–10 на сторону", "desc": "Противоположные рука и нога."}
    ],
    "feet": [
        {"name": "Короткая стопа", "file": "short_foot.jpg", "video_id": None, "sets": "3×12–15", "desc": "Подтягиваем свод стопы."},
        {"name": "Подъём на носки с разведением коленей", "file": "calf_raise_knees_out.jpg", "video_id": None, "sets": "3×15", "desc": "Колени наружу."},
        {"name": "Ходьба по массажному коврику", "file": "foot_massage_mat.jpg", "video_id": None, "sets": "5–7 минут", "desc": "По гальке или коврику."}
    ]
}

DATA_FILE = "workout_log.json"

def load_log():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_log(log):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)

# ==================== ИНТЕРФЕЙС ====================
st.title("🏋️‍♂️ Трекер ЛФК — Май 2026")
st.caption("Протрузия L5-S1 • Коксартроз • Плоскостопие")

tab1, tab2, tab3 = st.tabs(["📋 Программа", "🏋️‍♂️ Записать тренировку", "📊 История"])

with tab1:
    st.subheader("✅ Главные правила безопасности")
    st.warning("• Поясница всегда в **нейтральном положении**\n• Никаких глубоких наклонов вперёд и скручиваний\n• При боли в пояснице или ноге — сразу остановиться")
    
    st.subheader("Ежедневная разминка (5–7 мин)")
    for ex in exercises["warm_up"]:
        st.image(f"images/{ex['file']}", use_container_width=True)
        st.write(f"**{ex['name']}** — {ex['sets']}")
        st.write(ex['desc'])
        if ex.get("video_id"):
            st.video(f"https://www.youtube.com/embed/{ex['video_id']}")
        st.divider()
    
    st.subheader("Основной ЛФК-комплекс")
    for cat_name, cat_ex in [("Поясница", "lfk_core"), ("Тазобедренные", "lfk_hips"), ("Грудной отдел", "lfk_thoracic")]:
        st.markdown(f"**{cat_name}**")
        for ex in exercises[cat_ex]:
            st.image(f"images/{ex['file']}", use_container_width=True)
            st.write(f"**{ex['name']}** — {ex['sets']}")
            st.write(ex['desc'])
            if ex.get("video_id"):
                st.video(f"https://www.youtube.com/embed/{ex['video_id']}")
            st.divider()
    
    st.subheader("Упражнения для стоп")
    for ex in exercises["feet"]:
        st.image(f"images/{ex['file']}", use_container_width=True)
        st.write(f"**{ex['name']}** — {ex['sets']}")
        st.write(ex['desc'])
        if ex.get("video_id"):
            st.video(f"https://www.youtube.com/embed/{ex['video_id']}")
        st.divider()

# (остальная часть кода с tab2 и tab3 остаётся без изменений — просто скопируй весь код выше)

with tab2:
    # ... (весь код tab2 остаётся прежним, можешь оставить как было)

with tab3:
    # ... (весь код tab3 остаётся прежним)

st.sidebar.success("Приложение работает на iPhone!")
st.sidebar.caption("Версия май 2026 с видео")
