"use client";

import { useEffect, useState } from "react";
import axios from "axios";
import ReactMarkdown from "react-markdown";

export default function Home() {
  const [data, setData] = useState("");
  const [id, setId] = useState("");

  useEffect(() => {
    const id = window.location.pathname.slice(1);
    setId(id);

    const fetchData = async () => {
      try {
        const res = await axios.get(`http://localhost:8001/doc/${id}`);
        setData(res.data);
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
