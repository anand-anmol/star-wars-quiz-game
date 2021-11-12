import { useState } from 'react';
import './index.css';
import Intro from './components/Intro';
import Quiz from './components/Quiz';

const App = () => {

  const [start, setStart] = useState(false);

  return <div>

    <h1 className='text'>Star Wars Quiz Game</h1>

    { start ? <Quiz /> : <Intro setStart={setStart} />}

  </div>
}

export default App;
