import configData from "../config.json";

const EndScreen = ({ score }) => {

    const submitScore = async () => {

        const name = prompt("Please enter your Name");

        // POST to store score in database

        if (name !== null) {

            try {
                const response = await fetch(configData.SCORE_URL, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        "name": name,
                        "score": score
                    })
                })

                if (response.ok) {
                    console.log('Score saved successfully!');
                    window.location.reload();
                }
            }

            catch (error) {

                console.error(error);
                window.alert('Error getting questions. Please try again.')
            }

        }


    }

    /* Show user their score and render buttons to go back to menu
    and to save your score */

    return (
        <div>
            <h1> You scored {score} out of 5.</h1>

            <button onClick={() => window.location.reload()} >Back to Menu</button>

            <br />

            <button onClick={submitScore} >Click here to save your score.</button>

        </div>
    )
}

export default EndScreen;
