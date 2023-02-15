import { useState } from "react";

export default function useQuestions() {
  const getQuestions = () => {
    const qString = localStorage.getItem("questions");
    const userQ = JSON.parse(qString);
    return userQ;
  };

  const [questions, setQuestions] = useState(getQuestions());

  const saveQuestions = (questions) => {
    localStorage.setItem("questions", JSON.stringify(questions));
    setQuestions(questions);
  };

  return {
    setQuestions: saveQuestions,
    questions,
  };
}
