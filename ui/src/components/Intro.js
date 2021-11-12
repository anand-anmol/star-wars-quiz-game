const Intro = ({ setStart }) => {
    
    return (
        <div id='intro'>
            
            <h2 className='text'>
                Welcome to our quiz game!! 
                <br />
                Click the button to start the game.
            </h2>

            <button onClick= { () => setStart(true) }>
                Start!
            </button>

        </div >
    )
}

export default Intro;
