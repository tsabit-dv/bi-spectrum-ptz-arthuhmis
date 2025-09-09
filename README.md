# DS-2TD4538-25A4-W — Bi-Spectrum Mobile Thermal PTZ Camera (Artemis)

Repo ini berisi ringkasan pembelajaran & eksperimen programmer terhadap **Hikvision DS-2TD4538-25A4-W**, sebuah kamera **Bi-Spectrum Mobile Thermal PTZ**.

---

## 📌 Unit yang Dipelajari
- **Model**: DS-2TD4538-25A4-W  
- **Jenis**: Bi-Spectrum Mobile Thermal PTZ Camera  
- **Fitur Utama**:
  - Dual sensor: thermal (640×512 VOx) + visible (1920×1080)
  - PTZ control (Pan/Tilt/Zoom stabil di kondisi mobile)
  - Temperature measurement (hingga ±2°C akurasi)
  - Alarm suhu & deteksi kebakaran
  - Mendukung RTSP, ONVIF, ISAPI (Hikvision API)
  - Konektivitas mobile (4G/Wi-Fi/GPS)

---

## 🎯 Tujuan Pembelajaran
1. **Memahami arsitektur kamera bi-spectrum**
   - Cara kerja dual sensor (thermal + optik).
   - Peran PTZ untuk area monitoring bergerak (contoh: kendaraan patroli).

2. **Integrasi untuk Programmer**
   - Menggunakan **RTSP stream** untuk video real-time.
   - Mengakses **snapshot thermal & visible** melalui ISAPI.
   - Mengontrol **PTZ** (pan, tilt, zoom) via API.
   - Membaca & mengatur **temperature alarm**.
   - Membungkus API dalam **FastAPI Gateway** agar mudah digunakan sistem lain.

3. **Use Case**
   - Kendaraan patroli keamanan → monitoring mobile.
   - Pemadam kebakaran → deteksi titik panas.
   - Area industri → alarm suhu pipa/tangki.
   - GIS mapping → integrasi GPS kamera ke peta.

---

## 🛠️ Contoh API (ISAPI)

### Snapshot
- Visible:  
  `GET /ISAPI/Streaming/channels/101/picture`
- Thermal:  
  `GET /ISAPI/Streaming/channels/201/picture`

### PTZ Continuous Move
```xml
PUT /ISAPI/PTZCtrl/channels/1/continuous
<PTZData>
  <pan>0.5</pan>
  <tilt>0.0</tilt>
  <zoom>0.0</zoom>
</PTZData>
