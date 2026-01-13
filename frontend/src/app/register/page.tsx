"use client";
import React, { useState } from "react";
import { api } from "@/services/api";
import { useRouter } from "next/navigation";
import Layout from "../../components/Layout";

const RegisterPage: React.FC = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.post("/polls/register/", { username, password });
      router.push("/login");
    } catch (err: any) {
      setError(err.response?.data?.username || "Registration failed");
    }
  };

  return (
    <Layout>
      <h1 className="text-2xl font-bold mb-4">Register</h1>
      <form onSubmit={handleSubmit} className="max-w-sm space-y-4">
        {error && <p className="text-red-600">{error}</p>}
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="w-full p-2 border rounded"
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="w-full p-2 border rounded"
          required
        />
        <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">
          Register
        </button>
      </form>
    </Layout>
  );
};

export default RegisterPage;
