import streamlit as st
import json
import os
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="Трекер ЛФК • Май 2026", page_icon="🏋️‍♂️", layout="centered")

# ==================== УПРАЖНЕНИЯ ====================
exercises = {
    "warm_up": [
        {"name": "Ретракция подбородка", "file": "retraction_chin.jpg", "sets": "10×5 сек", "desc": "Подбородок слегка втягиваем назад."},
        {"name": "Мягкий наклон головы", "file": "head_tilt.jpg", "sets": "8–10 в каждую сторону", "desc": "Медленно, без рывков."},
        {"name": "Плечевые круги назад", "file": "shoulder_circles.jpg", "sets": "10 раз", "desc": "Раскрываем грудной отдел."},
        {"name": "Тазовые наклоны у стены", "file": "pelvic_tilt_standing.jpg", "sets": "10 раз", "desc": "Поясница прижимается к стене."}
    ],
    "lfk_core": [
        {"name": "Dead Bug (Мёртвый жук)", "file": "dead_bug.jpg", "sets": "3×8–10 на сторону", "desc": "Поясница прижата к полу. Главное упражнение при протрузии L5-S1."},
        {"name": "Тазовый наклон лёжа", "file": "pelvic_tilt_lying.jpg", "sets": "3×12–15", "desc": "Прижимаем поясницу к полу."},
        {"name": "Ягодичный мостик с подушкой", "file": "glute_bridge_pillow.jpg", "sets": "3×12–15", "desc": "Под колени — подушка, сильно сжимаем ягодицы."}
    ],
    "lfk_hips": [
        {"name": "Clamshell (Ракушка)", "file": "clamshell.jpg", "sets": "3×12–15 на сторону", "desc": "Стопы вместе, поднимаем верхнее колено."}
    ],
    "lfk_thoracic": [
        {"name": "Открытие грудной клетки", "file": "thoracic_opening.jpg", "sets": "3×45–60 сек", "desc": "На валике вдоль позвоночника."},
        {"name": "Superman", "file": "superman.jpg", "sets": "3×10–12", "desc": "Лёжа на животе."},
        {"name": "Bird-Dog", "file": "bird_dog.jpg", "sets": "3×8–10 на сторону", "desc": "Противоположные рука и нога."}
    ],
    "feet": [
        {"name": "Короткая стопа", "file": "short_foot.jpg", "sets": "3×12–15", "desc": "Подтягиваем свод стопы."},
        {"name": "Подъём на носки с разведением коленей", "file": "calf_raise_knees_out.jpg", "sets": "3×15", "desc": "Колени наружу."},
        {"name": "Ходьба по массажному коврику", "file": "foot_massage_mat.jpg", "sets": "5–7 минут", "desc": "По гальке или коврику."}
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
        st.divider()
    
    st.subheader("Основной ЛФК-комплекс")
    for cat_name, cat_ex in [("Поясница", "lfk_core"), ("Тазобедренные", "lfk_hips"), ("Грудной отдел", "lfk_thoracic")]:
        st.markdown(f"**{cat_name}**")
        for ex in exercises[cat_ex]:
            st.image(f"images/{ex['file']}", use_container_width=True)
            st.write(f"**{ex['name']}** — {ex['sets']}")
            st.write(ex['desc'])
            st.divider()
    
    st.subheader("Упражнения для стоп")
    for ex in exercises["feet"]:
        st.image(f"images/{ex['file']}", use_container_width=True)
        st.write(f"**{ex['name']}** — {ex['sets']}")
        st.write(ex['desc'])
        st.divider()

with tab2:
    st.subheader("Запись тренировки")
    workout_type = st.selectbox(
        "Тип тренировки",
        ["Разминка (5–7 мин)", "Основной ЛФК-комплекс", "Упражнения для стоп", "Плавание", "Короткая разминка + стопы"]
    )
    
    log_entry = {"date": datetime.now().strftime("%Y-%m-%d %H:%M"), "type": workout_type, "exercises": []}
    
    if "Разминка" in workout_type or "Короткая" in workout_type:
        cat = "warm_up"
    elif "ЛФК" in workout_type:
        cat = "lfk_core"
    elif "стоп" in workout_type.lower():
        cat = "feet"
    else:
        cat = None
    
    if cat and cat in exercises:
        for ex in exercises[cat]:
            st.image(f"images/{ex['file']}", caption=ex['name'], use_container_width=True)
            st.write(ex['desc'])
            
            col1, col2, col3 = st.columns(3)
            with col1:
                sets_done = st.text_input(f"Подходы ({ex['sets']})", value=ex['sets'], key=f"sets_{ex['name']}")
            with col2:
                reps_done = st.text_input("Повторения / время", key=f"reps_{ex['name']}")
            with col3:
                quality = st.selectbox("Правильность", ["Отлично", "Хорошо", "Средне", "Была ошибка", "Боль в пояснице"], key=f"q_{ex['name']}")
            
            note = st.text_input("Заметки", value="—", key=f"note_{ex['name']}")
            
            if st.button(f"✅ Сохранить {ex['name']}", key=f"save_{ex['name']}"):
                log_entry["exercises"].append({
                    "name": ex['name'],
                    "sets": sets_done,
                    "reps": reps_done,
                    "quality": quality,
                    "note": note
                })
                st.success(f"{ex['name']} сохранено!")
    
    if "Плавание" in workout_type:
        time = st.number_input("Минут плавания", min_value=10, max_value=60, value=25)
        style = st.text_input("Стиль", value="Кроль на спине")
        if st.button("✅ Сохранить плавание"):
            log_entry["exercises"].append({"name": "Плавание", "time": f"{time} мин", "style": style})
            st.success("Плавание сохранено!")
    
    if st.button("💾 Сохранить всю тренировку", type="primary"):
        if log_entry["exercises"] or "Плавание" in workout_type:
            log = load_log()
            log.append(log_entry)
            save_log(log)
            st.balloons()
            st.success("Тренировка успешно сохранена! 🎉")
        else:
            st.warning("Добавь хотя бы одно упражнение")

with tab3:
    st.subheader("История тренировок")
    log = load_log()
    if log:
        df = pd.DataFrame([
            {
                "Дата": entry["date"],
                "Тип": entry["type"],
                "Упражнений": len(entry["exercises"]),
                "Примечание": entry["exercises"][0]["note"] if entry["exercises"] else "—"
            } for entry in log
        ])
        st.dataframe(df.sort_values("Дата", ascending=False), use_container_width=True)
    else:
        st.info("Пока нет записанных тренировок")

st.sidebar.success("Приложение работает на iPhone!")
st.sidebar.caption("Версия май 2026")