"use client";
import React, {createContext, useState, useContext, ReactNode, useEffect} from "react";

interface AuthContextType {
  token: string | null;
  login: (token: string, username: string) => void;
  logout: () => void;
  username: string | null;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [token, setToken] = useState<string | null>(null);
  const [username, setUsername] = useState<string | null>(null);

  useEffect(() => {
    setToken(localStorage.getItem("token"));
    setUsername(localStorage.getItem("username"));
  }, []);

  const login = (t: string, username: string) => {
    localStorage.setItem("username", username);
    localStorage.setItem("token", t);
    setUsername(username);
    setToken(t);
  };

  const logout = () => {
    localStorage.removeItem("username");
    localStorage.removeItem("token");
    setToken(null);
    setUsername(null);
  };

  return <AuthContext.Provider value={{ token, login, logout, username }}>{children}</AuthContext.Provider>;
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error("useAuth must be used within AuthProvider");
  return context;
};
