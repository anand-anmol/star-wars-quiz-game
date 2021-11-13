import { useEffect, useState } from "react";
import configData from "../config.json";

const LeaderBoard = () => {

    // scores state to store past high scores
    const [scores, setScores] = useState([])

    useEffect(() => {

        const getScores = async () => {

            // get high scores from the API

            try {

                const res = await fetch(configData.LEADERBOARD_URL);
                const scores = await res.json();
                setScores(scores);

            } catch (error) {

                console.error(error);
                window.alert('Error getting scores. Please try again.')

            }

        }

        getScores();

    }, [])

    // Render past high scores into a table

    return (
        <div>
            <h2>Leader Board</h2>

            <table>
                <tbody>

                    <tr>
                        <th>Name</th><th>Score</th><th>Timestamp</th>
                    </tr>
                    {
                        scores.map((score, i) => (
                            <tr key={i}>
                                <td>{score.name}</td>
                                <td>{score.score}</td>
                                <td>{score.date_created}</td>
                            </tr>
                        ))
                    }
                </tbody>
            </table>

        </div>
    )
}


export default LeaderBoard
