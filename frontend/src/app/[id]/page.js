"use client";

import { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";

export default function Home() {
  const [data, setData] = useState("");
  const [id, setId] = useState("");

  useEffect(() => {
    const id = window.location.pathname.slice(1);
    setId(id);

    const fetchData = async () => {
      try {
        const res = await fetch(`http://localhost:8001/doc/${id}`);

        if (!res.ok) {
          throw new Error("Network response was not ok");
        }
        const ans = await res.json();
        setData(ans);
      } catch (err) {
        console.error("Failed to fetch:", err);
      }
    };

    fetchData();
  }, []);

  return (
    <div className="general">
      <div className="markdown">
        <ReactMarkdown>{data}</ReactMarkdown>
      </div>
    </div>
  );
}
