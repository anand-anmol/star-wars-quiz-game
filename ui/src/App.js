import { useState } from 'react';
import './index.css';
import Intro from './components/Intro';
import Quiz from './components/Quiz';
import LeaderBoard from './components/LeaderBoard';

const App = () => {

  // start state to switch from Intro to Quiz
  const [start, setStart] = useState(false);
  // start state to replace Intro with LeaderBoard
  const [leaderBoard, setLeaderBoard] = useState(false);
  
  /* Render Quiz if start state is true;
      else display button for show/hide leaderboard
      Render leaderboard if LeaderBoard state is true else render Intro */
  
  return <div>

    <h1 className='text'>Star Wars Quiz Game</h1>

    {start ? <Quiz /> :

      <>
        <button onClick={() => setLeaderBoard(!leaderBoard)}>
          {leaderBoard ? "Back to Game" : "Show Leader Board"}
        </button>
        {leaderBoard ? <LeaderBoard /> : <Intro setStart={setStart} />}
      </>

    }

  </div>

}

export default App;
