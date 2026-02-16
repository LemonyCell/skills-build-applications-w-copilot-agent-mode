import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, NavLink } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

const themeClasses = {
  default: {
    root: 'bg-white text-dark',
    nav: 'navbar navbar-expand-lg navbar-light bg-light',
    switchBtn: 'btn btn-outline-primary',
  },
  night: {
    root: 'bg-dark text-light',
    nav: 'navbar navbar-expand-lg navbar-dark bg-dark',
    switchBtn: 'btn btn-outline-light',
  },
};

function App() {
  const [theme, setTheme] = useState('default');

  const toggleTheme = () => {
    setTheme((prev) => (prev === 'default' ? 'night' : 'default'));
  };

  const current = themeClasses[theme];

  return (
    <Router>
      <div className={`App ${current.root} min-vh-100`}>
        <nav className={current.nav}>
          <div className="container-fluid">
            <NavLink className="navbar-brand" to="/">
              Octofit Tracker
            </NavLink>
            <button
              className="navbar-toggler"
              type="button"
              data-bs-toggle="collapse"
              data-bs-target="#navbarNav"
              aria-controls="navbarNav"
              aria-expanded="false"
              aria-label="Toggle navigation"
            >
              <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarNav">
              <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                <li className="nav-item">
                  <NavLink className="nav-link" to="/activities">
                    Activities
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className="nav-link" to="/leaderboard">
                    Leaderboard
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className="nav-link" to="/teams">
                    Teams
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className="nav-link" to="/users">
                    Users
                  </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink className="nav-link" to="/workouts">
                    Workouts
                  </NavLink>
                </li>
              </ul>
            </div>
            <div className="d-flex">
              <button className={current.switchBtn} onClick={toggleTheme}>
                Switch to {theme === 'default' ? 'Night' : 'Default'} Mode
              </button>
            </div>
          </div>
        </nav>

        <div className="container mt-4">
          <Routes>
            <Route path="/activities" element={<Activities />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/users" element={<Users />} />
            <Route path="/workouts" element={<Workouts />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
