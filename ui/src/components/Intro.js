import { useState } from 'react';
import LeaderBoard from './LeaderBoard';

const Intro = ({ setStart }) => {
    
    const [leaderBoard, setLeaderBoard] = useState(false);

    return (
        <div id='intro'>
            
            <h2 className='text'>
                Welcome to our quiz game!! 
                <br />
                Click the button to start the game.
            </h2>

            <button onClick= { () => setStart(true) }>
                Start Game!
            </button>

            <br />


            <button onClick= { () => setLeaderBoard(!leaderBoard) }>
                { leaderBoard ? "Hide" : "Show"} Leader Board
            </button>

            { leaderBoard ? <LeaderBoard /> : "" }

        </div >
    )
}

export default Intro;
