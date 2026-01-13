"use client";
import React, { useState } from "react";
import { api } from "@/services/api";
import { useRouter } from "next/navigation";
import { useAuth } from "@/context/AuthContext";
import Layout from "../../components/Layout";

const LoginPage: React.FC = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const router = useRouter();
  const { login } = useAuth();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await api.post("/auth/login/", { username, password });
      login(response.data.access, username);
      router.push("/");
    } catch {
      setError("Login failed");
    }
  };

  return (
    <Layout>
      <h1 className="text-2xl font-bold mb-4">Login</h1>
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
          Login
        </button>
      </form>
    </Layout>
  );
};

export default LoginPage;
