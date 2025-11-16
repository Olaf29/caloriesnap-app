import streamlit as st
import pandas as pd 

def display_nutrition_response(data: dict):
    try:
        nutrition = data.get('nutrition', {})
        
        st.markdown(
            f"<h2 style='text-align: center;'>{data.get('foodName', 'Makanan')}</h2>", 
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(
                label="Total Kalori",
                value=f"{nutrition.get('calories', 0)} kkal"
            )
        with col2:
            st.metric(
                label="Total Protein",
                value=f"{nutrition.get('protein', 0)} g"
            )
        with col3:
            st.metric(
                label="Total Karbohidrat",
                value=f"{nutrition.get('carbs', 0)} g"
            )
        with col4:
            st.metric(
                label="Total Lemak",
                value=f"{nutrition.get('fat', 0)} g"
            )
        
        st.divider() 

        components = data.get('components', [])
        if components:
            with st.expander("Lihat Rincian Komponen Makanan"):
                df = pd.DataFrame(components)
                df.columns = ["Nama Item", "Estimasi Porsi"]
                st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.caption("Tidak ada rincian komponen yang terdeteksi.")
        
        st.info(f"Catatan: {data.get('notes', 'Tidak ada catatan.')}", icon="💡")

    except Exception as e:
        st.error(f"Terjadi kesalahan saat menampilkan hasil: {e}")
        st.write("Data mentah dari AI:")
        st.json(data)

def handle_analysis_result(data: dict):
    display_nutrition_response(data)

    is_valid_food = True
    food_name_lower = data.get('foodName', '').lower()
    notes_lower = data.get('notes', '').lower()

    invalid_keywords = [
        "tidak ada makanan", 
        "tidak terdeteksi", 
        "bukan makanan", 
        "tidak dapat diidentifikasi",
        "manusia",
        "jempol",
        "tidak ada objek makanan"
    ]

    if any(keyword in food_name_lower for keyword in invalid_keywords):
        is_valid_food = False

    if any(keyword in notes_lower for keyword in invalid_keywords):
        is_valid_food = False

    if is_valid_food:
        st.session_state.history.insert(0, data)