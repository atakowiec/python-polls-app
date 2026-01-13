"use client"
import React from "react";
import { usePolls } from "@/hooks/usePolls";
import PollCard from "../components/PollCard";
import Layout from "../components/Layout";

const HomePage: React.FC = () => {
  const { polls, isLoading, isError } = usePolls();

  return (
    <Layout>
      <h1 className="text-3xl font-bold mb-6">Polls</h1>
      {isLoading && <p>Loading polls...</p>}
      {isError && <p>Error loading polls.</p>}
      {polls?.length ? (
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {polls.map((poll) => (
            <PollCard key={poll.id} poll={poll} />
          ))}
        </div>
      ) : (
        <p>No polls available.</p>
      )}
    </Layout>
  );
};

export default HomePage;
