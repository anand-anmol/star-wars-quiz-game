import { useEffect, useState } from "react";
import configData from "../config.json";
import Question from "./Question";
import EndScreen from "./EndScreen";

const Quiz = () => {

    const [questions, setQuestions] = useState([])
    const [score, setScore] = useState(0)

    useEffect( () => {

        const getQuestions = async () => {
            try {

                const res = await fetch(configData.QUESTIONS_URL);
                const questions = await res.json();
                setQuestions(questions);
    
            } catch (error) {

                console.error(error);
                
            }
        }

        getQuestions();

    }, [])

    const selectAnswer = (e) => {

        const chosenAnswer = e.target.innerText;

        if (chosenAnswer === questions[0].correct_answer) {
            setScore(score + 1);
        }

        setQuestions(questions.filter((item, index) => index !== 0));
   
    }

    return <div>
        
        { questions.length > 0 ? <Question question={questions[0]} selectAnswer={selectAnswer} /> : <EndScreen score={score} /> }
            
        </div>

}

export default Quiz;
