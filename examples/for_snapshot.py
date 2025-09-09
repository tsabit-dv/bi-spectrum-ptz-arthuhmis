"""
Contoh kontrol PTZ kamera Hikvision DS-2TD4538-25A4-W
via ISAPI (HTTP API).
"""

import requests
from requests.auth import HTTPBasicAuth

CAMERA_IP = "192.168.1.64"
USER = "admin"
PASS = "12345"

def move_pan_tilt(pan=0.0, tilt=0.0, zoom=0.0):
    """
    Gerakkan kamera secara continuous (akan berhenti sendiri setelah timeout vendor).
    pan, tilt, zoom bernilai -1.0 .. 1.0
    """
    url = f"http://{CAMERA_IP}/ISAPI/PTZCtrl/channels/1/continuous"
    body = f"""
    <PTZData>
        <pan>{pan}</pan>
        <tilt>{tilt}</tilt>
        <zoom>{zoom}</zoom>
    </PTZData>
    """.strip()
    r = requests.put(url, data=body, headers={"Content-Type": "application/xml"},
                     auth=HTTPBasicAuth(USER, PASS))
    print("Response:", r.status_code, r.text)

def stop():
    """
    Stop gerakan PTZ
    """
    url = f"http://{CAMERA_IP}/ISAPI/PTZCtrl/channels/1/continuous"
    body = "<PTZData><pan>0</pan><tilt>0</tilt><zoom>0</zoom></PTZData>"
    r = requests.put(url, data=body, headers={"Content-Type": "application/xml"},
                     auth=HTTPBasicAuth(USER, PASS))
    print("Stop:", r.status_code)

if __name__ == "__main__":
    # Contoh: pan ke kanan pelan
    move_pan_tilt(pan=0.5, tilt=0.0, zoom=0.0)
