const Question = ({ question, selectAnswer }) => {

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
