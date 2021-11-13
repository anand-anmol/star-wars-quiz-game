const Intro = ({ setStart }) => {

    // Render welcome text and a button to start the quiz

    return (
        <div id='intro'>

            <h2 className='text'>
                Welcome to our quiz game!!
                <br />
                Click the button to start the game.
            </h2>

            <button onClick={() => setStart(true)}>
                Start Game!
            </button>

        </div >
    )
}

export default Intro;
