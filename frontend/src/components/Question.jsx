import { useEffect, useState, Component } from "react";
import { useLocation } from "react-router-dom";
import HoverVideoPlayer from "react-hover-video-player";
// TODO: remove dependency
import ReactPlayer from "react-player";
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

  const tns = [
    require("../clips/tn_0.jpg"),
    require("../clips/tn_1.jpg"),
    require("../clips/tn_2.jpg"),
    require("../clips/tn_3.jpg"),
    require("../clips/tn_4.jpg"),
    require("../clips/tn_5.jpg"),
    require("../clips/tn_6.jpg"),
    require("../clips/tn_7.jpg"),
    require("../clips/tn_8.jpg"),
    require("../clips/tn_9.jpg"),
    require("../clips/tn_10.jpg"),
    require("../clips/tn_11.jpg"),
    require("../clips/tn_12.jpg"),
    require("../clips/tn_13.jpg"),
    require("../clips/tn_14.jpg"),
    require("../clips/tn_15.jpg"),
    require("../clips/tn_16.jpg"),
    require("../clips/tn_17.jpg"),
    require("../clips/tn_18.jpg"),
    require("../clips/tn_19.jpg"),
  ];

  console.log("url Value", question[0]);

  const sour = "./clp1.jpg";
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
                src={tns[question[0]]}
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
                //src={imgs[parseInt(question[2]) - 1]}
                src={tns[question[0] + 1]}
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
