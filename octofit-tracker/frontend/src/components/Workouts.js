import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);

  useEffect(() => {
    const fetchWorkouts = async () => {
      const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;
      console.log(`Fetching data from: ${endpoint}`);
      try {
        const response = await fetch(endpoint);
        const data = await response.json();
        console.log('Fetched workouts data:', data);
        setWorkouts(data.results || data);
      } catch (error) {
        console.error('Error fetching workouts:', error);
      }
    };

    fetchWorkouts();
  }, []);

  return (
    <div>
      <h1>Workouts</h1>
      <ul>
        {workouts.map((workout, index) => (
          <li key={index}>{workout.name || JSON.stringify(workout)}</li>
        ))}
      </ul>
    </div>
  );
};

export default Workouts;