import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Login from "./components/Login";
import Questions from "./components/Questions";
import Home from "./components/Home";
import useToken from "./components/useToken";
import useQuestions from "./components/useQuestions";

import { useEffect, useState } from "react";

import "./App.css";

function App() {
  const { token, setToken } = useToken();
  const { questions, setQuestions } = useQuestions();

  if (!token || !questions) {
    return <Login setToken={setToken} setQuestions={setQuestions} />;
  }

  return (
    <div className="wrapper">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route
            path="/questions"
            element={<Questions userName={token} questions={questions} />}
          />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
