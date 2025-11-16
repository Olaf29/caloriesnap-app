import streamlit as st
from PIL import Image
import json
from connect_api import get_gemini_model
from formatting import display_nutrition_response, handle_analysis_result

def get_nutrition_from_image(uploaded_file):
    model = get_gemini_model(use_json_schema=True) 
    
    if model is None:
        st.error("Model Gemini tidak berhasil dimuat. Periksa API Key Anda.")
        return 
    if uploaded_file is None:
        st.warning("Tidak ada file yang diunggah.")
        return 

    try:
        img = Image.open(uploaded_file)
        
        prompt_sistem = (
            "Anda adalah ahli gizi. Analisis gambar makanan ini secara mendetail. "
            "Identifikasi nama hidangannya, semua komponennya, dan hitung total nutrisi. "
            
            "**PENTING UNTUK PORSI:** Saat memperkirakan porsi (misal: '100 gram' atau '1 Piring'), "
            "**carilah objek referensi di dalam gambar** seperti sendok, garpu, gelas, atau tangan "
            "untuk membantu Anda menilai skala dan ukuran sebenarnya dari makanan tersebut. "
            "Jika tidak ada objek referensi, asumsikan porsi standar (misal: piring makan malam standar). "
            
            "Berikan jawaban Anda HANYA dalam format JSON yang diminta."
        )
        
        response = model.generate_content([prompt_sistem, img])
        data = json.loads(response.text)
        
        handle_analysis_result(data)
        
    except json.JSONDecodeError:
        st.error("Gagal membaca respons JSON dari AI. Coba unggah lagi.")
        try:
            st.error(f"Error: AI mengembalikan format tidak terduga.\nRespons mentah: {response.text}")
        except:
            st.error("Error: Gagal mem-parsing respons AI.")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memproses gambar: {e}")