"use client"

import useSWR from "swr";
import { api } from "@/services/api";
import { Poll } from "@/types/polls";

export const usePolls = () => {
  const { data, error, mutate } = useSWR<Poll[]>("/polls/", () =>
    api.get("/polls/").then(res => res.data)
  );

  return {
    polls: data,
    isLoading: !error && !data,
    isError: error,
    mutate,
  };
};
