from fastapi import FastAPI
from datetime import datetime, timezone, timedelta
from typing import Any
app = FastAPI()

@app.get("/")
def index():
    # Get current time in IST (UTC+5:30)
    ist_time = datetime.now(timezone(timedelta(hours=5, minutes=30)))
    return {"now": ist_time.strftime("%y-%m-%d : %H:%M:%S")}


@app.get("/date/{hh}-{mm}")
def get_timezone(hh: int, mm: int) -> Any:
    try:
        # Create a timezone with user-defined offset
        custom_time = datetime.now(timezone(timedelta(hours=hh, minutes=mm)))
        return {
            "custom_timezone": f"UTC+{hh:+02d}:{mm:02d}",
            "time": custom_time.strftime("%y-%m-%d : %H:%M:%S")
        }
    except Exception as e:
        return {"error": str(e)}
