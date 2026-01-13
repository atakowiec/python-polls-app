import React from "react";
import Link from "next/link";
import { useAuth } from "@/context/AuthContext";

interface LayoutProps {
  children: React.ReactNode;
}

const Layout: React.FC<LayoutProps> = ({ children }) => {
  const { token, logout } = useAuth();

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <header className="bg-blue-600 text-white p-4 flex justify-between items-center">
        <Link href="/">
          <h1 className="text-2xl font-bold cursor-pointer">Polls App</h1>
        </Link>
        <nav className="space-x-4">
          {token ? (
            <>
              <Link href="/profile" className="hover:underline">
                Profile
              </Link>
              <Link href="/create" className="hover:underline">
                Create Poll
              </Link>
              <button
                onClick={logout}
                className="hover:underline text-white"
              >
                Logout
              </button>
            </>
          ) : (
            <>
              <Link href="/login" className="hover:underline">
                Login
              </Link>
              <Link href="/register" className="hover:underline">
                Register
              </Link>
            </>
          )}
        </nav>
      </header>
      <main className="flex-1 container mx-auto p-4">{children}</main>
      <footer className="bg-gray-200 text-center p-2 text-sm">
        © 2026 Polls App
      </footer>
    </div>
  );
};

export default Layout;
