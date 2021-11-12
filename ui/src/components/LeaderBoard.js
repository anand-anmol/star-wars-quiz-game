import { useEffect, useState } from "react";
import configData from "../config.json";

const LeaderBoard = () => {

    const [scores, setScores] = useState([])

    useEffect(() => {

        const getScores = async () => {

            try {

                const res = await fetch(configData.LEADERBOARD_URL);
                const scores = await res.json();
                setScores(scores);

            } catch (error) {

                console.error(error);

            }

        }

        getScores();

    }, [])

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
