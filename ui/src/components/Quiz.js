import { useEffect, useState } from "react";
import configData from "../config.json";
import Question from "./Question";
import EndScreen from "./EndScreen";

const Quiz = () => {

    // questions state to store array with questions for quiz
    const [questions, setQuestions] = useState([])
    // state to store player's current score
    const [score, setScore] = useState(0)

    useEffect(() => {

        const getQuestions = async () => {

            try {

                // Make get request to get questions for the quiz
                const res = await fetch(configData.QUESTIONS_URL);
                const questionsFromAPI = await res.json();
                setQuestions(questionsFromAPI);

            } catch (error) {

                console.error(error);
                window.alert('Error getting questions. Please try again.')
                window.location.reload();

            }
        }

        getQuestions();

    }, [])

    const selectAnswer = (e) => {

        const chosenAnswer = e.target.innerText;

        // if chosen answer is correct, increment score
        if (chosenAnswer === questions[0].correct_answer) {
            setScore(score + 1);
        }

        // remove first question in questions array
        setQuestions(questions.filter((item, index) => index !== 0));

    }

    /* if there are questions in the questions array, render question
    with first question else render endscreen */

    return <div>

        <h3>Current Score: {score}/5</h3>

        {questions.length > 0 ? <Question question={questions[0]} selectAnswer={selectAnswer} /> : <EndScreen score={score} />}

    </div>

}

export default Quiz;
