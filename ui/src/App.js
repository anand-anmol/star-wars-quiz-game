import { useState } from 'react';
import './index.css';
import Intro from './components/Intro';
import Quiz from './components/Quiz';
import LeaderBoard from './components/LeaderBoard';

const App = () => {

  const [start, setStart] = useState(false);
  const [leaderBoard, setLeaderBoard] = useState(false);

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
