"use client";
import React, { useState } from "react";
import { usePoll } from "@/hooks/usePoll";
import OptionList from "../../../components/OptionList";
import Layout from "../../../components/Layout";
import { api } from "@/services/api";
import { useWebSocket } from "@/hooks/useWebSocket";
import ServerStatus from "../../../components/ServerStatus";
import {useParams, useRouter} from "next/navigation";


const PollDetailPage: React.FC = () => {
  const params = useParams();
  const pollId = Number(params.id);
  const { poll, isLoading, isError, mutate } = usePoll(pollId);
  const [votingDisabled, setVotingDisabled] = useState(false);
  const router = useRouter();

  useWebSocket(`${process.env.NEXT_PUBLIC_WS_URL}/polls/${pollId}/`, (data) => {
    if (poll) {
      mutate({...poll, options: data.message.options}, false);
    }
  }, [poll?.id]);

  const handleVote = async (optionId: number) => {
    try {
      setVotingDisabled(true);
      await api.post(`/polls/${pollId}/vote/`, { option_id: optionId });
    } finally {
      setVotingDisabled(false);
    }
  };

  if (isLoading) return <Layout>Loading poll...</Layout>;
  if (isError || !poll) return <Layout>Poll not found.</Layout>;

  return (
    <Layout>
      <ServerStatus />
      <h1 className="text-2xl font-bold mb-4">{poll.title}</h1>
      <p className="text-gray-700 mb-4">{poll.description}</p>
      <OptionList options={poll.options} onVote={handleVote} disabled={!poll.is_active || votingDisabled} />
      <p className="mt-2 text-sm text-gray-500">
        Status: {poll.is_active ? "Active" : "Closed"} | Created: {new Date(poll.created_at).toLocaleString()}
      </p>
      <button
        className="mt-4 text-blue-600 underline hover:no-underline cursor-pointer"
        onClick={() => router.push("/")}
      >
        ← Back to Polls
      </button>
    </Layout>
  );
};

export default PollDetailPage;
