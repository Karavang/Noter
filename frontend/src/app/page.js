"use client";

import { useState } from "react";
import Modal from "./components/modalWindow";

export default function Home() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  return (
    <div className="general mainPage">
      <div className="menu">
        <button>userinfo</button>

        <button>Add new one</button>
        <button>Preferences</button>
        <button onClick={() => setIsModalOpen(true)}>Open Modal</button>

        <Modal
          isOpen={isModalOpen}
          onClose={() => setIsModalOpen(false)}
        >
          <h2>Modal Title</h2>
          <p>This is the content inside the modal.</p>
        </Modal>
        {/* <button className="getPremium">Get Premium</button> */}
      </div>
      <div className="list">sadsa</div>
    </div>
  );
}
