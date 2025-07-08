"use client";

import { useEffect, useState } from "react";
import Modal from "./components/modalWindow";

export default function Home() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [backWidth, setBackWidth] = useState(1366);
  const handleFileChange = (event) => {
    const file = event.target.files[0];

    if (file) {
      const reader = new FileReader();

      reader.onloadend = () => {
        const image = new Image();

        image.onload = () => {
          const width = image.width;
          const height = image.height;

          console.log(`Image size: ${width}x${height}px`);

          document.body.style.backgroundImage = `url(${reader.result})`;
          setBackWidth(width);
        };

        image.src = reader.result;
      };

      reader.readAsDataURL(file);
    }
  };
  useEffect(() => {
    const screenWidth = window.innerWidth;
    if (screenWidth < backWidth) {
      document.body.style.backgroundSize = "auto";
    } else {
      document.body.style.backgroundSize = "cover";
    }
  }, [backWidth]);
  return (
    <div className="general mainPage">
      <div className="menu">
        <button className="buttonMenu">userinfo</button>

        <button className="buttonMenu">Add new one</button>

        <button
          onClick={() => setIsModalOpen(true)}
          className="buttonMenu"
        >
          Preferences
        </button>

        <Modal
          isOpen={isModalOpen}
          onClose={() => setIsModalOpen(false)}
        >
          <div className="preferences">
            <div>
              Change background:{" "}
              <button
                onClick={() => document.getElementById("fileInput").click()}
              >
                Select image
              </button>
              <input
                id="fileInput"
                text="file"
                type="file"
                onChange={handleFileChange}
                accept=".png, .jpg, .jpeg"
                style={{ display: "none" }}
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
