import React from "react";
import {Poll} from "@/types/polls";
import Link from "next/link";
import {useAuth} from "@/context/AuthContext";
import {api} from "@/services/api";

interface PollCardProps {
  poll: Poll;
}

const PollCard: React.FC<PollCardProps> = ({poll}) => {
  const {token, username} = useAuth();

  const handleDelete = async (e: React.MouseEvent) => {
    e.stopPropagation(); // prevent navigating to poll page
    if (!token) return alert("You must be logged in to delete");
    if (!confirm("Are you sure you want to delete this poll?")) return;

    try {
      console.log(token)
      await api.delete(`/polls/${poll.id}/delete/`, {
        headers: {Authorization: `Bearer ${token}`},
      });
      window.location.reload(); // refresh list after deletion
    } catch (err) {
      console.error(err);
      alert("Failed to delete poll");
    }
  };

  const isOwner = poll.owner === username; // check if current user owns this poll

  return (
    <div className="bg-white p-4 rounded-lg shadow hover:shadow-lg transition cursor-pointer relative">
      <Link href={`/polls/${poll.id}`}>
        <h2 className="text-xl font-bold mb-2">{poll.title}</h2>
        <p className="text-gray-600 mb-2">{poll.description}</p>
        <p className="text-sm text-gray-500">
          Status: {poll.is_active ? "Active" : "Closed"} | Created:{" "}
          {new Date(poll.created_at).toLocaleString()}
        </p>
      </Link>
      {isOwner && (
        <button
          onClick={handleDelete}
          className="absolute top-2 right-2 bg-red-500 text-white px-2 py-1 rounded hover:bg-red-600"
        >
          Delete
        </button>
      )}
    </div>
  );
};

export default PollCard;
