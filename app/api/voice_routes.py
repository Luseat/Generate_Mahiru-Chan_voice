from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
# from app.services.tts_service import generate_base_tts
# from app.services.rvc_service import process_rvc


router = APIRouter()


class TexttoVoiceRequest(BaseModel):
    text: str
    voice: str = "id"
    

@router.post("/text-to-voice")
async def generate_text_to_voice(req: TexttoVoiceRequest):
    try:
        #1. Generate Base TTS (suara manusia biasa tapi pelafalan natural)
        # base_audio_path = await generate_base_tts(req.text, req.voice)
        
        
        #2. Convert dengan RVC jadi suara Mahiru
        # mahiru_audio_path = await process_rvc(base_audio_path)
        
        
        return {"status": "success", "message": f"Teks '{req.text}' memproses menjadi suara Mahiru Shiina..."}
    
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@router.post("/voice-to-voice")
async def generate_voice_to_voice(audio_file: UploadFile = File(...)):
    if not audio_file.filename.endswith(('.wav', '.mp3', '.ogg')):
        raise HTTPException(status_code=400, detail="Format audio harus WAV, MP3, atau OGG.")
    
    
    # di sini simpan file audionya dan panggil RVC
    return {"status": "success", "message": "Audio diterima, siap dikonversi ke suara Mahiru Shiina..."}