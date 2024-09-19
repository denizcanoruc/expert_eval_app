import { useEffect, useState } from "react";
import ReactPlayer from "react-player";

function Home({ setToken }) {
  const pathway = window.location.href;
  const [fin, setFin] = useState(false);
  const [play, setPlay] = useState(false);
  const [play2, setPlay2] = useState("");

  const handleLogout = (e) => {
    setFin(true);
  };
  const handleHooverIn = (e) => {
    setPlay(true);
  };
  const handleHooverOut = (e) => {
    setPlay(false);
  };
  const handlePause = (e) => {
    console.log("Yey");
  };

  console.log(pathway);
  return (
    <div className="App">
      <header className="App-header">
        <p>
          {!fin && "Welcome! Here is a small tutorial:"} {fin && "Goodbye!"}{" "}
        </p>
        <ReactPlayer url="./tutorial.mp4" controls={true} />

        {!fin && (
          <a
            className="App-link"
            href={pathway + "questions"}
            target="_blank"
            rel="noopener noreferrer"
            onClick={handleLogout}
          >
            Start
          </a>
        )}
      </header>
      ;
    </div>
  );
}

export default Home;
