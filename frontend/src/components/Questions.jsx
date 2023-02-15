import Container from "react-bootstrap/Container";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Question from "./Question";
import { useEffect, useState } from "react";
import axios from "axios";
import ProgressBar from "react-bootstrap/ProgressBar";
import Button from "react-bootstrap/Button";
//const baseURL = "http://127.0.0.1:3000";
//const baseURL = "https://b14c-2a02-2c40-200-b001-00-1-4eeb.eu.ngrok.io";

function Questions({ userName, questions }) {
  const [qNo, setQNo] = useState(1);
  const [curAnswer, setCurAnswer] = useState(3);
  const [answerList, setAnswerList] = useState([3, 3, 3, 3, 3, 3, 3, 3, 3, 3]);
  const qList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].map((number) => (
    <Question
      question={questions[number]}
      setAnswer={setCurAnswer}
      key={number}
      answer={answerList[number]}
    />
  ));

  const handleBarClick = (e) => {
    setQNo(parseInt(e.target.getAttribute("qval")));
  };

  const progBars = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].map((number) => (
    <ProgressBar
      animated={number == qNo - 1}
      variant={answerList[number] == 3 ? "warning" : "success"}
      label={(number + 1).toString()}
      now={10}
      qval={number + 1}
      onClick={handleBarClick}
      key={number}
    />
  ));

  const handleCont = async (e) => {
    console.log(curAnswer);
    e.preventDefault();
    if (curAnswer !== 3) {
      const temp = await axios.post("/questions_back", {
        question_id: questions[qNo - 1][0],
        username: userName,
        answer: curAnswer,
      });
      answerList[qNo - 1] = curAnswer;
      setAnswerList(answerList);
      setQNo(qNo + 1);
      setCurAnswer(3);
    } else {
      setQNo(qNo + 1);
    }
    //isAuth.data === "YES" ? navigate("/question") : console.log(isAuth);
  };

  const handleFin = (e) => {
    console.log("Completed");
    localStorage.clear();
    window.close();
  };
  // useEffect(() => {}, [curAnswer]);

  console.log(qNo);

  if (qNo <= 10) {
    return (
      <div className="App">
        <header className="App-header">
          <Container>
            <Row>
              <ProgressBar>{progBars}</ProgressBar>
            </Row>
            <Row style={{ margin: 10 }}> </Row>
            {qList[qNo - 1]}
            <Row style={{ margin: 10 }}> </Row>
            <Row>
              <Button onClick={handleCont} id="cont_but">
                Continue
              </Button>
            </Row>
          </Container>
        </header>
      </div>
    );
  } else {
    return (
      <div className="App">
        <header className="App-header">
          <Container>
            <Row>
              <ProgressBar>{progBars}</ProgressBar>
            </Row>
            <Row style={{ margin: 10 }}> </Row>
            <p>{answerList.includes(3) && "INCOMPLETE FORM"}</p>
            <p>{!answerList.includes(3) && "THANK YOU"}</p>
            <Row style={{ margin: 10 }}> </Row>
            <Row>
              <Button
                onClick={handleFin}
                id="cont_but"
                disabled={answerList.includes(3)}
              >
                Finish
              </Button>
            </Row>
          </Container>
        </header>
      </div>
    );
  }
}

// TODO: Be sure to use it

export default Questions;
