"use client"
import { useEffect, useRef } from "react";

export const useWebSocket = (
  url: string,
  onMessage: (data: any) => void,
  deps: any[] = []
) => {
  const ws = useRef<WebSocket | null>(null);

  useEffect(() => {
    ws.current = new WebSocket(url);
    console.log(`Connecting to: ${url}`)

    ws.current.onmessage = (event) => {
      const data = JSON.parse(event.data);
      onMessage(data);
    };

    ws.current.onerror = (err) => {
      console.error(err);
    }

    ws.current.onclose = () => {
      console.log(`Connection closed: ${url}`);
    }

    return () => {
      console.log(`Disconnected from: ${url}`)
      ws.current?.close();
    };
  }, [url, ...deps]);
};
