import edge_tts
import os
import uuid


TEMP_AUDIO_DIR = "temp_audio"
os.makedirs(TEMP_AUDIO_DIR, exist_ok=True)


async def generate_base_tts(text: str, voice_lang: str = "id") -> str:
    """
    Fungsi ini bakal ngubah teks jadi suara manusia biasa dulu (Tahap 1)
    """


    # Suara berdasarkan bahasa
    if voice_lang == "id":
        voice_model =  "id-ID-GadisNeural"
    elif voice_lang == "en":
        voice_model = "en-US-GuyNeural"
    else:
        voice_model =  "id-ID-GadisNeural"
    
    
    filename = f"{uuid.uuid4()}.mp3"
    filepath = os.path.join(TEMP_AUDIO_DIR, filename)
    
    
    try:
        communicate = edge_tts.Communicate(text, voice_model)
        await communicate.save(filepath)
        
        
        return filepath
    
    
    except Exception as e:
        raise Exception(f"Gagal generate TTS: {str(e)}")
        