import streamlit as st
import google.generativeai as genai
import os

NUTRITION_SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "foodName": {
            "type": "STRING", 
            "description": "Nama hidangan utama yang teridentifikasi, contoh: 'Nasi Goreng Komplit' atau 'Nasi, Ayam, dan Kangkung'"
        },
        "components": {
            "type": "ARRAY",
            "description": "Daftar rinci komponen/item makanan yang terlihat atau dideskripsikan.",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "item": {"type": "STRING", "description": "Nama item, contoh: 'Telur Mata Sapi' atau 'Nasi Putih'"},
                    "portion": {"type": "STRING", "description": "Estimasi porsi item ini, contoh: '1 Butir' atau '1 Piring'"}
                },
                "required": ["item", "portion"]
            }
        },
        "nutrition": {
            "type": "OBJECT",
            "description": "Estimasi nutrisi total untuk keseluruhan hidangan.",
            "properties": {
                "calories": {"type": "NUMBER", "description": "Total kalori dalam kkal (angka saja)"},
                "protein": {"type": "NUMBER", "description": "Total protein dalam gram (angka saja)"},
                "carbs": {"type": "NUMBER", "description": "Total karbohidrat dalam gram (angka saja)"},
                "fat": {"type": "NUMBER", "description": "Total lemak dalam gram (angka saja)"}
            },
            "required": ["calories", "protein", "carbs", "fat"]
        },
        "notes": {
            "type": "STRING", 
            "description": "Catatan singkat atau paragraf analisis, contoh: 'Kalori utama berasal dari nasi goreng yang berminyak dan telur.'"
        }
    },
    "required": ["foodName", "components", "nutrition", "notes"]
}

@st.cache_resource
def get_gemini_model(use_json_schema=False):
    """
    Menginisialisasi dan mengembalikan model Gemini.
    Jika use_json_schema=True, konfigurasikan model untuk JSON mode.
    """
    try:
        api_key = st.secrets.get("GEMINI_API_KEY")
        if not api_key:
            api_key = os.environ.get("GEMINI_API_KEY")
        
        if not api_key:
            st.error("GEMINI_API_KEY tidak ditemukan. Harap atur di Streamlit Secrets (secrets.toml).")
            return None

        genai.configure(api_key=api_key)
        
        generation_config = None
        if use_json_schema:
            generation_config = {
                "response_mime_type": "application/json",
                "response_schema": NUTRITION_SCHEMA
            }

        model = genai.GenerativeModel(
            "gemini-2.5-flash-preview-09-2025",
            generation_config=generation_config
        )
        return model
    
    except Exception as e:
        st.error(f"Gagal menginisialisasi model Gemini: {e}")
        return None