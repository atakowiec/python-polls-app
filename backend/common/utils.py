from datetime import datetime, timezone
from typing import Dict, Any
import os
import platform
import time


START_TIME = time.time()


def get_server_status() -> Dict[str, Any]:
    return {
        "status": "ok",
        "datetime": datetime.now(tz=timezone.utc).isoformat(),
        "uptime_seconds": int(time.time() - START_TIME),
        "python_version": platform.python_version(),
        "platform": platform.system(),
        "platform_release": platform.release(),
        "process_id": os.getpid(),
        "timezone": "UTC",
    }
