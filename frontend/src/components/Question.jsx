import { useEffect, useState, Component } from "react";
import { useLocation } from "react-router-dom";
import HoverVideoPlayer from "react-hover-video-player";
import ReactPlayer from "react-player";
import React from "react";

// TODO: remove dependency
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import MultiStepProgressBar from "./MultiStepProgressBar/MultiStepProgressBar";

function Question({ question, setAnswer, answer }) {
  const [whichSelected, setSelected] = useState(answer);

  const handleSelect = (e) => {
    console.log("TEST Value", parseInt(e.target.value));
    setSelected(parseInt(e.target.value));
    setAnswer(parseInt(e.target.value));
  };

  console.log("url Value", question);

  return (
    <Row>
      <Col>
        <label>
          <input
            type="radio"
            name="options"
            value={0}
            checked={whichSelected === 0}
            onChange={handleSelect}
          ></input>
          <HoverVideoPlayer
            videoSrc={question[1]}
            pausedOverlay={
              <img
                //src={imgs[parseInt(question[2]) - 1]}
                src={question[2]}
                alt=""
                style={{
                  // Make the image expand to cover the video's dimensions
                  width: "100%",
                  height: "100%",
                  objectFit: "cover",
                }}
              />
            }
            restartOnPaused={true}
            loop={true}
          />
        </label>
      </Col>
      <Col>
        <label>
          <input
            type="radio"
            name="options"
            value={1}
            checked={whichSelected === 1}
            onChange={handleSelect}
          ></input>
          <HoverVideoPlayer
            videoSrc={question[3]}
            pausedOverlay={
              <img
                src={question[4]}
                alt=""
                style={{
                  // Make the image expand to cover the video's dimensions
                  width: "100%",
                  height: "100%",
                  objectFit: "cover",
                }}
              />
            }
            restartOnPaused={true}
            loop={true}
          />
        </label>
      </Col>
    </Row>
  );
}

export default Question;

// TODO: Be sure to use it
