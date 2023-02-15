import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import PropTypes from "prop-types";

// const baseURL = "http://127.0.0.1:3000";
//const baseURL = "https://b14c-2a02-2c40-200-b001-00-1-4eeb.eu.ngrok.io";

function Login({ setToken, setQuestions }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isWrong, setIsWrong] = useState(false);

  const handleUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const isAuth = await axios.post("/login", {
      username,
      password,
    });
    console.log(isAuth);
    if (isAuth.data === "YES") {
      setToken(username);
      const data = await axios.get("/questions_back");
      console.log("DATA", data.data);
      setQuestions(
        data.data.map((q) => [q.question_id, q.url1, q.tn1, q.url2, q.tn2])
      );
    } else {
      console.log(isAuth);
      setIsWrong(true);
    }
  };

  return (
    <div className="form-group row">
      <header className="App-header">
        <p style={{ color: "red" }}>
          {isWrong && "You entered an incorrect username or password"}
        </p>
        <ul>
          <form className="form-inline" onSubmit={handleSubmit}>
            <label
              className="col-sm-2 col-form-label col-form-label-lg"
              htmlFor="username"
            >
              Username
            </label>
            <input
              className="form-control form-control-lg"
              onChange={handleUsernameChange}
              type="text"
              name="username"
              id="username"
              value={username}
            ></input>
            <label
              className="col-sm-2 col-form-label col-form-label-lg"
              htmlFor="password"
            >
              Password
            </label>
            <input
              className="form-control form-control-lg"
              onChange={handlePasswordChange}
              type="text"
              name="password"
              id="password"
              value={password}
            ></input>
            <label></label>
            <button className="form-control form-control-lg" type="submit">
              Submit
            </button>
          </form>
        </ul>
      </header>
    </div>
  );
}

Login.propTypes = {
  setToken: PropTypes.func.isRequired,
};

export default Login;
