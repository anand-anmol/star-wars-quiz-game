import configData from "../config.json";

const EndScreen = ({score}) => {

    const submitScore = async () => {

        const name = prompt("Please enter your Name");

        if (name !== null){

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


    }

    return (
        <div>
            <h1> You scored {score} out of 5.</h1>

            <button onClick={() => window.location.reload()} >Back to Menu</button>

            <br />

            <button onClick={submitScore} >Click here to save your score.</button>

        </div>
    )
}

export default EndScreen
