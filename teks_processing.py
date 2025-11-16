import streamlit as st
import json
from connect_api import get_gemini_model
from formatting import display_nutrition_response, handle_analysis_result

def get_nutrition_from_text(user_text):
    model = get_gemini_model(use_json_schema=True) 

    if model is None:
        st.error("Model Gemini tidak berhasil dimuat. Periksa API Key Anda.")
        return 
    if not user_text:
        st.warning("Silakan masukkan deskripsi makanan.")
        return 

    try:
        prompt = (
            "Anda adalah ahli gizi. Seorang pengguna memasukkan deskripsi makanan: "
            f"\"{user_text}\". Tafsirkan teks ini (walaupun non-formal), "
            "identifikasi nama hidangannya, semua komponennya, perkirakan porsinya, dan hitung total nutrisinya. "
            "Berikan jawaban Anda HANYA dalam format JSON yang diminta."
        )
        
        response = model.generate_content(prompt)
        data = json.loads(response.text)
        
        handle_analysis_result(data)
        
    except json.JSONDecodeError:
        st.error("Gagal membaca respons JSON dari AI. Coba masukkan teks lagi.")
        try:
            st.error(f"Error: AI mengembalikan format tidak terduga.\nRespons mentah: {response.text}")
        except:
            st.error("Error: Gagal mem-parsing respons AI.")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memproses teks: {e}")