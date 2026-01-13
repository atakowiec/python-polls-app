from datetime import datetime, timezone
from typing import Dict, Any


def get_server_status() -> Dict[str, Any]:
    return {
        "status": "ok",
        "datetime": datetime.now(tz=timezone.utc).isoformat(),
    }
