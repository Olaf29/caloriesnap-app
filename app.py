import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64
from image_processing import get_nutrition_from_image
from teks_processing import get_nutrition_from_text
from formatting import display_nutrition_response

try:
    page_icon_image = Image.open("images/ckal2.png")
except FileNotFoundError:
    page_icon_image = "🥗"

def get_image_as_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

@st.cache_data
def load_css(file_name):
    """
    Membaca file CSS dan MENGEMBALIKAN isinya.
    Hasilnya akan di-cache oleh Streamlit.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        st.error(f"File CSS '{file_name}' tidak ditemukan. Pastikan file ada di direktori yang sama.")
        return ""
    except Exception as e:
        st.error(f"Gagal memuat CSS: {e}")
        return ""

try:
    avatar_base64 = get_image_as_base64("images/shidqi.png")
    avatar_src = f"data:image/png;base64,{avatar_base64}"
except FileNotFoundError:
    avatar_src = "https://via.placeholder.com/150/0000FF/FFFFFF?text=Shidqi"

st.set_page_config(
    page_title="CalorieSnap",
    page_icon=page_icon_image,
    layout="wide",
    initial_sidebar_state="collapsed"
)

if 'history' not in st.session_state:
    st.session_state.history = []

css_content = load_css("style.css")
st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)

selected = option_menu(
    menu_title=None,
    options=["Beranda", "Hitung Kalori", "Riwayat", "Tentang"],
    icons=["house-fill", "calculator-fill", "clock-history", "person-circle"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "transparent"},
        "icon": {"font-size": "30px"},
        "nav-link": {
            "font-size": "30px",
            "color": "#4CAF50",
            "text-align": "center",
            "margin": "0px 5px",
            "padding": "18px 28px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {
            "font-size": "30px",
            "background-color": "#4CAF50",
            "color": "white",
            "border-radius": "12px",
            "padding": "18px 2px",
        },
    },
)

# Halaman Beranda
if selected == "Beranda":
    
    st.markdown("<h1 style='text-align: center; font-size: 3.5rem; color: #4CAF50;'>CalorieSnap — Hitung Kalori Seketika</h1>", unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center; font-size: 1.25rem; max-width: 700px; margin: 1rem auto 2rem auto;'>Unggah foto atau ketik deskripsi makanan/minuman Anda. AI akan menghitung kalori dan makronutrien secara otomatis, cepat, dan akurat.</p>", unsafe_allow_html=True)
        
    st.divider()

    st.markdown("<h2 style='text-align: center; padding-top: 1rem;'>Fitur Utama</h2>", unsafe_allow_html=True)
    col_f1, col_f2, col_f3, col_f4 = st.columns(4)
    with col_f1:
        st.markdown("<div class='feature-highlight'><span>📸</span><strong>Analisis Foto Otomatis</strong><p>AI mendeteksi makanan/minuman dari foto secara instan.</p></div>", unsafe_allow_html=True)
    with col_f2:
        st.markdown("<div class='feature-highlight'><span>📝</span><strong>Analisis Deskripsi Teks</strong><p>Cukup deskripsikan makanan/minuman Anda.</p></div>", unsafe_allow_html=True)
    with col_f3:
        st.markdown("<div class='feature-highlight'><span>🔍</span><strong>Estimasi Nutrisi Detail</strong><p>Dapatkan estimasi kalori, karbohidrat, protein, dan lemak Anda.</p></div>", unsafe_allow_html=True)
    with col_f4:
        st.markdown("<div class='feature-highlight'><span>⚡</span><strong>Hasil Cepat & Akurat</strong><p>Didukung oleh model AI generatif canggih.</p></div>", unsafe_allow_html=True)
    st.divider()

    st.markdown("<h2 style='text-align: center; padding-top: 1rem;' id='demo-cara-kerja'>Cara Kerja</h2>", unsafe_allow_html=True)
    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1:
        st.markdown("<div class='step-card'><h3>1️⃣ Unggah Foto / Ketik</h3><p>Pilih metode input yang paling Anda sukai di tab 'Hitung Kalori'.</p></div>", unsafe_allow_html=True)
    with col_s2:
        st.markdown("<div class='step-card'><h3>2️⃣ AI Mengenali & Menghitung</h3><p>AI menganalisis input Anda dalam hitungan detik.</p></div>", unsafe_allow_html=True)
    with col_s3:
        st.markdown("<div class='step-card'><h3>3️⃣ Hasil Detail Ditampilkan</h3><p>Dapatkan rincian kalori dan makronutriennya.</p></div>", unsafe_allow_html=True)
    st.divider()

    st.markdown("<h2 style='text-align: center; padding-top: 1rem;'>Edukasi</h2>", unsafe_allow_html=True)
    col_e1, col_e2, col_e3, col_e4 = st.columns(4)
    with col_e1:
        st.markdown("""
        <div class="edu-card">
            <h4>📚 Apa itu Kalori?</h4>
            <p>Kalori adalah energi yang dibutuhkan tubuh untuk beraktivitas.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_e2:
         st.markdown("""
        <div class="edu-card">
            <h4>🍗 Apa itu Makronutrien?</h4>
            <p>Nutrisi yang dibutuhkan tubuh dalam jumlah besar, meliputi:
               <b>Protein</b> → membangun otot<br>
               <b>Karbohidrat</b> → sumber energi utama<br>
               <b>Lemak sehat</b> → membantu hormon & fungsi otak</p>
        </div>
        """, unsafe_allow_html=True)
    with col_e3:
         st.markdown("""
        <div class="edu-card">
            <h4>🥗 Porsi Makan yang Tepat</h4>
            <p>½ piring sayur<br>
               ¼ protein<br>
               ¼ karbohidrat<br>
               Hindari gorengan berlebihan.</p>
        </div>
        """, unsafe_allow_html=True)
    with col_e4:
         st.markdown("""
        <div class="edu-card">
            <h4>🚶 Gaya Hidup Seimbang</h4>
            <p>Minum 8 gelas air<br>
               30 menit olahraga<br>
               Kurangi gula tambahan<br>
               Tidur yang cukup.</p>
        </div>
        """, unsafe_allow_html=True)
    st.divider()

    st.markdown("<h2 style='text-align: center; padding-top: 1rem;'>Pertanyaan Umum (FAQ)</h2>", unsafe_allow_html=True)
    
    col_faq_L, col_faq_M, col_faq_R = st.columns([1, 2, 1])
    with col_faq_M:
        with st.expander("Apakah harus login?"):
           st.write("Tidak. Aplikasi ini bisa langsung dipakai tanpa perlu mendaftar atau login.")
    
        with st.expander("Seberapa akurat estimasinya?"):
           st.write(
               "Estimasi dihitung menggunakan **Gemini**, model AI canggih dari Google. "
               "Sangat baik untuk penggunaan sehari-hari dengan toleransi wajar, namun tetap merupakan estimasi, bukan pengganti analisis lab medis."
           )
    
        with st.expander("Apakah aplikasi ini gratis?"):
           st.write("Ya, versi dasar aplikasi ini gratis untuk digunakan.")
    
        with st.expander("Apakah bisa mendeteksi makanan/minuman Indonesia?"):
           st.write(
               "Ya! Berkat kemampuan multimodal Gemini, aplikasi ini dapat mengenali berbagai hidangan termasuk makanan/minuman Indonesia seperti Nasi Goreng, Rendang, Gado-gado, dan lainnya."
           )

# Halaman Hitung Kalori
elif selected == "Hitung Kalori":
    
    st.markdown("<h1 style='text-align: center;'>Analisis Kalori & Nutrisi</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Pilih metode input Anda. Unggah foto atau ketik deskripsi makanan/minuman Anda.</p>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Analisis via Foto 📸", "Analisis via Teks ✍️"])

    # --- Analisis Foto ---
    with tab1:
        st.markdown("<h3 style='text-align: center;'>Foto Makanan/Minuman Anda</h3>", unsafe_allow_html=True)
        image_file = None
        col_radio_left, col_radio_mid, col_radio_right = st.columns([1, 2, 1])
        with col_radio_mid:
            input_method = st.radio(
                "Pilih metode input foto:",
                ["Unggah File 📁", "Ambil Foto 📸"],
                horizontal=True,
                label_visibility="collapsed"
            )
        col_img_left, col_img_mid, col_img_right = st.columns([1, 2, 1]) 
        with col_img_mid: 
            if input_method == "Unggah File 📁":
                image_file = st.file_uploader(
                    "Pilih gambar makanan/minuman (format JPG, JPEG, atau PNG)",
                    type=["jpg", "jpeg", "png"],
                    label_visibility="collapsed"
                )
                if image_file is not None:
                    st.image(image_file, width=550)
            elif input_method == "Ambil Foto 📸":
                image_file = st.camera_input(
                    "Arahkan kamera ke makanan/minuman Anda, lalu klik tombol 📸",
                    key="camera_input_calorie",
                    label_visibility="collapsed"
                )
        if image_file is not None: 
            col_left, col_mid, col_right = st.columns([1, 2, 1])
            with col_mid:
                if st.button(
                    " Analisis ", 
                    key="btn_analisis_gambar",
                    type="primary",
                    use_container_width=True
                ): 
                    with st.spinner("Sedang menganalisis... Mohon tunggu..."):
                        try:
                            get_nutrition_from_image(image_file) 
                        except Exception as e:
                            st.error(f"Gagal menganalisis: {e}")

    # --- Analisis Teks ---
    with tab2:
        st.markdown("<h3 style='text-align: center;'>Deskripsi Makanan/Minuman Anda</h3>", unsafe_allow_html=True)
        
        col_left_txt, col_mid_txt, col_right_txt = st.columns([1, 2, 1])
        with col_mid_txt:
            user_text_input = st.text_area(
                "Label (disembunyikan)", 
                height=150,
                placeholder="Contoh: 'nasi putih 1 piring, paha ayam goreng, dan semangkuk kecil tumis kangkung'",
                label_visibility="collapsed"
            )
            
            if st.button(
                " Analisis ", 
                key="btn_analisis_teks",
                type="primary",
                use_container_width=True
            ): 
                if user_text_input:
                    with st.spinner("Sedang menganalisis... Mohon tunggu..."):
                        try:
                            get_nutrition_from_text(user_text_input)
                        except Exception as e:
                            st.error(f"Gagal menganalisis: {e}")
                else:
                    st.warning("Silakan masukkan deskripsi makanan/minuman terlebih dahulu.")

# Halaman Riwayat
elif selected == "Riwayat":

    def remove_history_item(index_to_remove):
        """Callback untuk menghapus item dari session state berdasarkan indeksnya."""
        try:
            del st.session_state.history[index_to_remove]
        except IndexError:
            st.error("Gagal menghapus item, indeks tidak ditemukan.")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
            
    if not st.session_state.history:
        st.markdown(
            """
            <div class="empty-history-card">
                <h3>🥗 Riwayat Anda Masih Kosong</h3>
                <p>
                    Anda belum memiliki riwayat analisis. <br>
                    Silakan buka tab <strong>'Hitung Kalori'</strong> untuk memulai!
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(f"### Anda memiliki **{len(st.session_state.history)}** catatan riwayat:")
        
        for index, item_data in enumerate(st.session_state.history):
            
            food_name = item_data.get('foodName', 'Tanpa Nama')
            calories = item_data.get('nutrition', {}).get('calories', 0)
            
            with st.expander(f"**{food_name}** — Estimasi Kalori **{calories} kkal**"):
            
                display_nutrition_response(item_data)
                
                col_btn_left, col_btn_right = st.columns([4, 1])
                with col_btn_right:
                    st.button(
                        label="Hapus",
                        key=f"delete_btn_{index}",
                        on_click=remove_history_item,
                        args=(index,),
                        type="secondary"
                    )
        
        st.markdown("---") 
        col_l, col_m, col_r = st.columns([2, 1, 2])
        with col_m:
            if st.button(
                "Hapus Semua Riwayat", 
                type="primary", 
                use_container_width=True, 
                key="btn_hapus_semua"
            ):
                st.session_state.history = []
                st.rerun()

# Halaman Tentang
elif selected == "Tentang":
    
    st.markdown("<h1 style='text-align: center;'>Tentang CalorieSnap</h1>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <p style='text-align: center; font-size: 1.15rem; max-width: 800px; margin: 1rem auto;'>
        CalorieSnap adalah platform cerdas yang membantu Anda menghitung kalori dan makronutrien 
        secara otomatis hanya dari foto atau deskripsi makanan/minuman. 
        <br><br>
        Dibangun dengan teknologi AI mutakhir, aplikasi ini dirancang untuk 
        membuat hidup sehat menjadi lebih mudah, cepat, dan praktis.
        </p>
        """, 
        unsafe_allow_html=True
    )
    
    st.divider()
    
    st.markdown("<h2 style='text-align: center; margin-top: 2rem;'>Pengembang</h2>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="profile-card">
            <span class="profile-card-avatar">
                <img src="{avatar_src}" alt="Shidqi Naufal">
            </span>
            <h3>Shidqi Naufal</h3>
            <p>23051130026</p>
            <div class="social-links">
                <a href="https://github.com/Olaf29" title="GitHub"> <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub Logo">
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.divider() 
    
    st.markdown("<h2 style='text-align: center; margin-top: 2rem;'>Teknologi yang Digunakan</h2>", unsafe_allow_html=True)
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown("""
        <div class="step-card" style="padding: 1.5rem 2rem; text-align: left;">
            <h4 style="text-align: center; font-size: 1.1rem;">Bahasa & Framework</h4>
            <ul>
                <li>Python</li>
                <li>Streamlit</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col_t2:
        st.markdown("""
        <div class="step-card" style="padding: 1.5rem 2rem; text-align: left;">
            <h4 style="text-align: center; font-size: 1.1rem;">AI & Model</h4>
            <ul>
                <li>Google Gemini API</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider() 

    st.markdown("<h2 style='text-align: center; margin-top: 2rem;'>Kontak</h2>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style='text-align: center; font-size: 1.1rem; max-width: 600px; margin: 1rem auto;'>
        Ada pertanyaan, saran, atau ingin berkolaborasi? Jangan ragu untuk menghubungi!
        </p>
        """, 
        unsafe_allow_html=True
    )

    col_left, col_mid, col_right = st.columns([1, 2, 1])
    with col_mid:
        st.markdown(
            """
            <div class="feature-highlight">
                <span>📧</span>
                <strong>Email</strong>
                <p>shidqi2naufal9@gmail.com</p>
            </div>
            """, 
            unsafe_allow_html=True
        )