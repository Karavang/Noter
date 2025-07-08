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

        <button onClick={() => setIsModalOpen(true)}>Preferences</button>

        <Modal
          isOpen={isModalOpen}
          onClose={() => setIsModalOpen(false)}
        >
          <div className="preferences">
            <div>
              Change background:
              <input
                type="file"
                accept=".png, .jpg, .jpeg"
              />
            </div>
          </div>
        </Modal>
        {/* <button className="getPremium">Get Premium</button> */}
      </div>
      <div className="list">sadsa</div>
    </div>
  );
}
