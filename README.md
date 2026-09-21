# Generate Mahiru~Chan Voice

API Backend berbasis **FastAPI** untuk melakukan generasi suara menggunakan model **RVC (Retrieval-based Voice Conversion)**. API ini dirancang khusus untuk menghasilkan suara karakter **Mahiru Shiina** dari anime *The Angel Next Door Spoils Me Rotten*, dengan intonasi dan pelafalan bahasa Indonesia/Inggris yang natural.

##  Fitur Utama
- **Text-to-Voice (T2V)**: Menggunakan pendekatan *2-step pipeline* (Edge-TTS sebagai *base voice*, kemudian di-convert menggunakan RVC agar pelafalan bahasa Indonesia tidak kaku).
- **Voice-to-Voice (V2V)**: Mengkonversi rekaman suara *user* menjadi suara Mahiru secara langsung dengan mempertahankan emosi dan intonasi asli.

## 📂 Struktur Project
```text
mahiru_voice/
│
├── app/
│   ├── api/
│   │   └── voice_routes.py    # Endpoint API (T2V & V2V)
│   ├── services/
│   │   └── tts_service.py     # Logika Tahap 1 (Edge-TTS)
│   └── main.py                # Entry point FastAPI & konfigurasi server
│
├── temp_audio/                # Folder penyimpanan audio sementara (ter-ignore git)
├── venv/                      # Virtual environment (ter-ignore git)
├── .gitignore                 # File konfigurasi abaikan git
├── requirements.txt           # Dependencies project
└── README.md                  # Dokumentasi project
```

##  Instalasi & Setup

1. **Clone repository ini**
   ```bash
   git clone <URL_REPO_LU>
   cd mahiru_voice
   ```

2. **Buat & Aktifkan Virtual Environment (Windows)**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan Server API**
   ```bash
   uvicorn app.main:app --reload
   ```

Server akan berjalan di `http://127.0.0.1:8000`.

## 📖 Endpoint Dokumentasi
Setelah server berjalan,  bisa mengakses dokumentasi interaktif Swagger UI di:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

### Endpoint Tersedia:
- `GET /` : Cek status server.
- `POST /api/v1/text-to-voice` : Mengubah teks menjadi suara Mahiru.
- `POST /api/v1/voice-to-voice` : Mengubah file audio *user* menjadi suara Mahiru.

## 📝 Catatan
Proyek ini masih dalam tahap pengembangan. Tahap saat ini baru mengimplementasikan Tahap 1 (Base TTS menggunakan Edge-TTS).


---
<p align="center">Copyright &copy; 2026 Hanifudin Robbani | All Rights Reserved.</p>