const Question = ({ question, selectAnswer }) => {

    // Render question text and options as buttons

    return <div>
        <h2>{question.question}</h2>

        {question.options.map((option) => (

            <div key={option}>
                <button onClick={selectAnswer}> {option} </button>
                <br />
            </div>

        ))}
    </div>
}

export default Question;
