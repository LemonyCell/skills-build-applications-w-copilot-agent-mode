import React, { useEffect, useState } from 'react';

const Leaderboard = () => {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    const fetchLeaderboard = async () => {
      const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/`;
      console.log(`Fetching data from: ${endpoint}`);
      try {
        const response = await fetch(endpoint);
        const data = await response.json();
        console.log('Fetched leaderboard data:', data);
        setLeaderboard(data.results || data);
      } catch (error) {
        console.error('Error fetching leaderboard:', error);
      }
    };

    fetchLeaderboard();
  }, []);

  return (
    <div>
      <h1>Leaderboard</h1>
      <ul>
        {leaderboard.map((entry, index) => (
          <li key={index}>{entry.name || JSON.stringify(entry)}</li>
        ))}
      </ul>
    </div>
  );
};

export default Leaderboard;