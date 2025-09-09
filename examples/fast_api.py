from fastapi import FastAPI
from pydantic import BaseModel
import requests
from requests.auth import HTTPBasicAuth

CAMERA_IP = "192.168.1.64"
USER = "admin"
PASS = "12345"

app = FastAPI(title="Artemis PTZ API Demo")

class PTZMove(BaseModel):
    pan: float = 0.0
    tilt: float = 0.0
    zoom: float = 0.0

@app.get("/snapshot/{channel}")
def snapshot(channel: int):
    """
    Ambil snapshot dari channel (101 = visible, 201 = thermal)
    """
    url = f"http://{CAMERA_IP}/ISAPI/Streaming/channels/{channel}/picture"
    r = requests.get(url, auth=HTTPBasicAuth(USER, PASS))
    if r.status_code == 200:
        return {"status": "ok", "size": len(r.content)}
    return {"status": "error", "code": r.status_code}

@app.post("/ptz/move")
def move(data: PTZMove):
    url = f"http://{CAMERA_IP}/ISAPI/PTZCtrl/channels/1/continuous"
    body = f"""
    <PTZData>
        <pan>{data.pan}</pan>
        <tilt>{data.tilt}</tilt>
        <zoom>{data.zoom}</zoom>
    </PTZData>
    """.strip()
    r = requests.put(url, data=body, headers={"Content-Type": "application/xml"},
                     auth=HTTPBasicAuth(USER, PASS))
    return {"status": r.status_code, "response": r.text}
