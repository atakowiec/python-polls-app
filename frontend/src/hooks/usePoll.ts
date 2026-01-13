"use client"
import { api } from "@/services/api";
import { Poll } from "@/types/polls";
import useSWR from "swr";

export const usePoll = (id: number) => {
  const { data, error, mutate } = useSWR<Poll>(`/polls/${id}/`, () =>
    api.get(`/polls/${id}/`).then(res => res.data)
  );

  return {
    poll: data,
    isLoading: !error && !data,
    isError: error,
    mutate,
  };
};
