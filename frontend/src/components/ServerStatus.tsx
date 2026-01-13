import React, { useState } from "react";
import { useWebSocket } from "@/hooks/useWebSocket";

const ServerStatus: React.FC = () => {
  const [status, setStatus] = useState<{ status: string; datetime: string } | null>(null);

  useWebSocket(`${process.env.NEXT_PUBLIC_WS_URL}/status/`, (data) => setStatus(data));

  return (
    <div className="p-2 text-sm text-gray-700 border rounded mb-4">
      Server status: {status?.status || "loading"} | Time: {status?.datetime || "--"}
    </div>
  );
};

export default ServerStatus;
