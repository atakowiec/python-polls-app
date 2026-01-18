import React, { useState } from "react";
import { useWebSocket } from "@/hooks/useWebSocket";

type ServerStatusData = {
  status: string;
  datetime: string;
  uptime_seconds: number;
  python_version: string;
  platform: string;
  platform_release: string;
  process_id: number;
  timezone: string;
};

const ServerStatus: React.FC = () => {
  const [status, setStatus] = useState<ServerStatusData | null>(null);

  useWebSocket(`${process.env.NEXT_PUBLIC_WS_URL}/status/`, (data) =>
    setStatus(data)
  );

  return (
    <div className="p-2 text-sm text-gray-700 border rounded mb-4 space-y-1">
      <div>
        <strong>Status:</strong> {status?.status || "loading"}
      </div>
      <div>
        <strong>Time:</strong> {status?.datetime || "--"}
      </div>
      <div>
        <strong>Uptime:</strong>{" "}
        {status ? `${status.uptime_seconds}s` : "--"}
      </div>
      <div>
        <strong>Python Version:</strong> {status?.python_version || "--"}
      </div>
      <div>
        <strong>Platform:</strong> {status?.platform || "--"}{" "}
        {status?.platform_release || ""}
      </div>
      <div>
        <strong>Process ID:</strong> {status?.process_id || "--"}
      </div>
      <div>
        <strong>Timezone:</strong> {status?.timezone || "--"}
      </div>
    </div>
  );
};

export default ServerStatus;
