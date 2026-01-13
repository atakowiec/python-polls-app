"use client";
import React, { useState } from "react";
import { api } from "@/services/api";
import { useAuth } from "@/context/AuthContext";
import { useRouter } from "next/navigation";
import Layout from "../../components/Layout";

const CreatePollPage: React.FC = () => {
  const { token } = useAuth();
  const router = useRouter();

  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [isActive, setIsActive] = useState(true);
  const [options, setOptions] = useState<string[]>(["", ""]); // start with 2 empty options
  const [error, setError] = useState("");

  const handleOptionChange = (index: number, value: string) => {
    const newOptions = [...options];
    newOptions[index] = value;
    setOptions(newOptions);
  };

  const addOption = () => setOptions([...options, ""]);
  const removeOption = (index: number) =>
    setOptions(options.filter((_, i) => i !== index));

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!token) return setError("You must be logged in");

    // filter out empty options
    const filteredOptions = options.map((o) => o.trim()).filter(Boolean);
    if (filteredOptions.length < 2) return setError("Add at least 2 options");

    try {
      await api.post(
        "/polls/create/",
        { title, description, is_active: isActive, options: filteredOptions },
        { headers: { Authorization: `Bearer ${token}` } }
      );
      router.push("/");
    } catch (err: any) {
      setError("Failed to create poll");
      console.error(err);
    }
  };

  return (
    <Layout>
      <h1 className="text-2xl font-bold mb-4">Create Poll</h1>
      <form onSubmit={handleSubmit} className="max-w-md space-y-4">
        {error && <p className="text-red-600">{error}</p>}

        <input
          type="text"
          placeholder="Poll Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="w-full p-2 border rounded"
          required
        />

        <textarea
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="w-full p-2 border rounded"
          required
        />

        <label className="flex items-center space-x-2">
          <input
            type="checkbox"
            checked={isActive}
            onChange={(e) => setIsActive(e.target.checked)}
          />
          <span>Active</span>
        </label>

        <div>
          <h2 className="font-semibold mb-2">Options</h2>
          {options.map((opt, index) => (
            <div key={index} className="flex items-center space-x-2 mb-2">
              <input
                type="text"
                placeholder={`Option ${index + 1}`}
                value={opt}
                onChange={(e) => handleOptionChange(index, e.target.value)}
                className="flex-1 p-2 border rounded"
                required
              />
              {options.length > 2 && (
                <button
                  type="button"
                  onClick={() => removeOption(index)}
                  className="text-red-600 font-bold"
                >
                  ×
                </button>
              )}
            </div>
          ))}
          <button
            type="button"
            onClick={addOption}
            className="text-blue-600 hover:underline mt-2"
          >
            + Add Option
          </button>
        </div>

        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded mt-4"
        >
          Create
        </button>
      </form>
    </Layout>
  );
};

export default CreatePollPage;
