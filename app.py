import streamlit as st
import random

# 1. Создаем три вкладки (Рівень 1)
tab1, tab2, tab3 = st.tabs(["📱 Главная", "🛠️ Инструмент", "🔗 Корисні посилання"])

with tab1:
    st.title("Вкладка 1")
    st.write("Здесь ваш старый код для первой вкладки")

with tab2:
    st.title("Вкладка 2")
    st.write("Здесь ваш старый код для второй вкладки")

# 2. Наполняем третью вкладку ссылками и игрой (Рівень 1 и Рівень 3)
with tab3:
    st.header("🔗 Корисні посилання")
    
    # Две колонки для ссылок
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📚 Навчання")
        st.markdown("- 🌐 [W3Schools](https://w3schools.com) — Туторіали")
        st.markdown("- 🐍 [Python.org](https://python.org) — Офіційний сайт")
    with col2:
        st.markdown("### 🎮 Розваги")
        st.markdown("- 👾 [CodeCombat](https://codecombat.com) — Код граючи")
        st.markdown("- 🧩 [Chess.com](https://chess.com) — Шахи")

    st.markdown("---") # Разделитель

    # Логика игры "Вгадай число"
    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False

    st.subheader("🎲 Гра: Вгадай число від 1 до 100")
    
    with st.container(border=True):
        user_guess = st.number_input("Твій варіант:", min_value=1, max_value=100, step=1)
        
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("Перевірити", use_container_width=True):
                st.session_state.attempts += 1
                if user_guess < st.session_state.secret_number:
                    st.info("📈 Загадане число БІЛЬШЕ!")
                elif user_guess > st.session_state.secret_number:
                    st.info("📉 Загадане число МЕНШЕ!")
                else:
                    st.success(f"🎉 Перемога! Число {st.session_state.secret_number} за {st.session_state.attempts} спроб!")
                    st.session_state.game_over = True
                    
        with btn_col2:
            if st.button("Зіграти знову", use_container_width=True):
                st.session_state.secret_number = random.randint(1, 100)
                st.session_state.attempts = 0
                st.session_state.game_over = False
                st.rerun()
