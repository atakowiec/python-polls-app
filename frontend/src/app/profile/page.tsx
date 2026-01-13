"use client";
import React, { useEffect, useState } from "react";
import Layout from "../../components/Layout";
import { useAuth } from "@/context/AuthContext";
import { api } from "@/services/api";
import PollCard from "../../components/PollCard";
import {Poll} from "@/types/polls";

const ProfilePage: React.FC = () => {
  const { token, username } = useAuth();
  const [polls, setPolls] = useState<Poll[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!token) return;
    api
      .get("/polls/me/", { headers: { Authorization: `Bearer ${token}` } })
      .then((res) => setPolls(res.data))
      .finally(() => setLoading(false));
  }, [token]);

  console.log(polls)
  const handleDelete = async (id: number) => {
    if (!token) return;
    await api.delete(`/polls/${id}/delete/`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    setPolls(polls.filter((p) => p.id !== id));
  };

  if (!token) return <Layout>Please log in to view your profile</Layout>;
  if (loading) return <Layout>Loading...</Layout>;

  return (
    <Layout>
      <h1 className="text-2xl font-bold mb-4">Profile</h1>
      <p className="mb-4">Username: {username}</p>
      {polls.length ? (
        <div className="space-y-4">
          {polls.map((poll) => (
            <div key={poll.id} className="relative">
              <PollCard poll={poll} />
              <button
                className="absolute top-2 right-2 text-red-600 hover:underline"
                onClick={() => handleDelete(poll.id)}
              >
                Delete
              </button>
            </div>
          ))}
        </div>
      ) : (
        <p>You haven’t created any polls yet.</p>
      )}
    </Layout>
  );
};

export default ProfilePage;
