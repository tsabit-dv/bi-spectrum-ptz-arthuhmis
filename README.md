# DS-2TD4538-25A4-W — Bi-Spectrum Mobile Thermal PTZ Camera (Artemis)

Repo ini mendokumentasikan pembelajaran teknis integrasi **Hikvision DS-2TD4538-25A4-W** ke dalam sistem pihak ketiga.  
Fokusnya adalah bagaimana programmer dapat **mengambil data, video, alarm, dan mengontrol PTZ** melalui API.

---

## 🔎 Ringkasan Teknis

- **Model**: DS-2TD4538-25A4-W (Bi-Spectrum Mobile Thermal PTZ)
- **Sensor**:
  - Thermal: 640 × 512 VOx, NETD < 35 mK
  - Visible: 1920 × 1080 (Full HD), optical zoom
- **Fungsi utama**:
  - Dual stream (thermal + visible)
  - PTZ: Pan/Tilt/Zoom stabil untuk mobilitas
  - Suhu: pengukuran & alarm threshold
  - Deteksi kebakaran/anomali
  - GPS, Wi-Fi, 4G untuk mobilitas
- **Protokol & API**:
  - RTSP (stream video)
  - ISAPI (HTTP REST-like API Hikvision)
  - ONVIF (kontrol PTZ standar)
  - SDK vendor (opsional, C/C++/C#/Java)

---

## 📡 Data & Fungsi yang Bisa Diambil oleh Sistem Pihak Ketiga

### 🎥 Video & Snapshot
- **RTSP Stream**
  - Channel 101 → visible (optical)
  - Channel 201 → thermal
  - Contoh URL:  
    ```
    rtsp://<user>:<pass>@<ip-kamera>/Streaming/Channels/101
    rtsp://<user>:<pass>@<ip-kamera>/Streaming/Channels/201
    ```
- **Snapshot (ISAPI)**  
GET /ISAPI/Streaming/channels/101/picture # visible
GET /ISAPI/Streaming/channels/201/picture # thermal


### 🎛️ Kontrol PTZ
- **Continuous Move**  
PUT /ISAPI/PTZCtrl/channels/1/continuous
<PTZData>
<pan>0.5</pan>
<tilt>0.0</tilt>
<zoom>0.0</zoom>
</PTZData>

- **Stop PTZ**  
PUT /ISAPI/PTZCtrl/channels/1/continuous
<PTZData><pan>0</pan><tilt>0</tilt><zoom>0</zoom></PTZData>

- **Preset Position** (via ONVIF atau ISAPI) → bisa disimpan & dipanggil ulang.

### 🌡️ Data Thermal & Alarm
- **Temperature Status**  
GET /ISAPI/Thermal/channels/2/temperatureStatus

- **Set Alarm Rule**  
PUT /ISAPI/Thermal/channels/2/temperatureAlarms/1
<TemperatureAlarm>
<enabled>true</enabled>
<upperLimit>120</upperLimit>
<lowerLimit>-20</lowerLimit>
<regionID>1</regionID>
</TemperatureAlarm>

- Event alarm dapat dikirim kamera ke **webhook / alarm server** pihak ketiga.

### 📍 Metadata & Telemetri
- **GPS Data** → bisa diambil dari API sistem mobile camera.
- **System Status**  
GET /ISAPI/System/status

untuk info kesehatan perangkat.

---

## 🛠️ Integrasi ke Sistem Pihak Ketiga

Dengan data & fungsi di atas, programmer bisa:

1. **Monitoring video real-time**  
 - Ambil stream RTSP → tampilkan di aplikasi web/desktop/mobile.
 - Gunakan snapshot → integrasi ke dashboard SCADA/IoT.

2. **Kontrol Kamera PTZ**  
 - Buat UI untuk pan/tilt/zoom sesuai kebutuhan operator.
 - Simpan preset posisi untuk akses cepat.

3. **Analitik Thermal & Alarm**  
 - Konsumsi API `temperatureStatus` → tampilkan data suhu.
 - Integrasi alarm suhu → trigger notifikasi (Telegram, email, MQTT).

4. **Integrasi GIS & Mobile**  
 - Ambil GPS kamera → tampilkan posisi kamera di peta.
 - Cocok untuk armada patroli & mobil pemadam.

5. **Big Data / AI**  
 - Simpan snapshot + metadata suhu → analisis tren.
 - Integrasikan dengan OpenCV/YOLO untuk deteksi objek.

---

## 📂 Folder `examples/`

- `ptz_control.py` → script kontrol PTZ (pan/tilt/zoom).
- `snapshot.py` → ambil snapshot visible & thermal.
- `fastapi_api.py` → API Gateway lokal (FastAPI) untuk integrasi mudah dengan sistem lain.

---

## 🚀 Next Steps

- Kembangkan **dashboard web** → dual view (thermal + visible).
- Implementasi **AI deteksi kebakaran/anomali suhu**.
- Integrasi **notifikasi real-time** ke sistem pihak ketiga (MQTT, webhook, Telegram).
- Logging ke database untuk **analisis jangka panjang**.

---

⚠️ **Catatan**: Semua contoh API menggunakan **Basic Auth**. Gantilah `admin:12345` dengan kredensial sebenarnya & pastikan akses aman.
Reference
https://assets.hikvision.com/prd/public/all/doc/m000072194/DS-2TD4538-25A4_W_Datasheet_en-US_20231118.pdf
https://www.scribd.com/document/834366266/Hikvision-Isapi-2-0-Ptz-Service
