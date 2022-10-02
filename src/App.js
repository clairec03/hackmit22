import { useState, useEffect } from "react";
import { useAuthState } from "react-firebase-hooks/auth";
import ReactPlayer from "react-player/youtube";
import toast from "react-hot-toast";

import { auth } from "./lib/firebase";
import getTimestamps from "./lib/firestore/getTimestamps";

import MultipleChoice from "./components/MultipleChoice";
import PointDisplay from "./components/PointDisplay";
import Box from "@mui/material/Box";
import LinearProgress from "@mui/material/LinearProgress";
import "./globals.css";

import GoogleButton from "react-google-button";
import { googleSignIn } from "./lib/auth";
import getUser from "./lib/firestore/getUser";
import addUser from "./lib/firestore/addUser";
import addPoints from "./lib/firestore/addPoints";

function App() {
    const [user] = useAuthState(auth);

    const lesson = "Wormholes";

    const [segments, setSegments] = useState([]); // segments are sorted
    const getSegmentsOnStart = async () => {
        setSegments(await getTimestamps(lesson));
    };

    const [currentSegment, setCurrentSegment] = useState(null);

    const popupDelay = 20;
    const [seconds, setSeconds] = useState(0.0);

    const [progress, setProgress] = useState(100);

    const [points, setPoints] = useState(-99);

    useEffect(() => {
        const checkUser = async () => {
            if (user) {
                const profile = await getUser(user.email);
                if (!profile) {
                    addUser(user.email);
                    setPoints(0);
                } else {
                    console.log(profile);
                    setPoints(profile.points);
                }
            } else {
                setPoints(-99);
            }
        };
        checkUser();
    }, [user]);

    const randomizeSetCurrentSegment = (sg) => {
        let answers = sg.options.slice();
        answers.push(sg.answer.slice());
        for (let i = 3; i >= 0; i--) {
            // Fischer-Yates shuffle
            let j = Math.floor(Math.random() * (i + 1));
            let tmp = answers[i];
            answers[i] = answers[j];
            answers[j] = tmp;
        }
        setCurrentSegment({
            ...sg,
            options: answers.slice(), // pushes answer into the options and randomizes
        });
    };

    const resetSegment = () => {
        setCurrentSegment(null);
        setSegments(segments.slice(1)); // removes the first element
        setProgress(100);
    };

    const handleCorrectAnswer = () => {
        const pointsAdded = Math.ceil(progress / 10); // points 0-10
        addPoints(user.email, pointsAdded);
        setPoints(points + pointsAdded);
        resetSegment();
    };

    const handleProgress = (secs) => {
        setSeconds(Math.floor(secs));
        if (
            currentSegment !== null &&
            seconds - currentSegment.seconds >= popupDelay
        ) {
            resetSegment();
            return;
        }
        if (currentSegment === null) {
            for (let i = 0; i < segments.length; i++) {
                if (segments[i].seconds <= seconds) {
                    randomizeSetCurrentSegment(segments[i]);
                }
            }
        }
    };

    const vidUrl = "https://www.youtube.com/watch?v=9P6rdqiybaw";

    useEffect(() => {
        const timer = setInterval(() => {
            setProgress((oldProgress) => {
                if (!currentSegment) {
                    return oldProgress;
                }
                return Math.max(oldProgress - 1, 0);
            });
        }, popupDelay * 8);
        return () => {
            if (currentSegment) {
                if (progress < 1) {
                    toast.error("Time ran out, sorry!")
                }
                resetSegment();
            }
            clearInterval(timer);
        };
    // eslint-disable-next-line
    }, [currentSegment]);

    if (user) {
        return (
            <div className="center">
                <ReactPlayer
                    url={vidUrl}
                    playing={true}
                    volume={1}
                    width="75vw"
                    height="75vh"
                    onProgress={(e) => handleProgress(e.playedSeconds)}
                    onStart={getSegmentsOnStart}
                />
                {currentSegment && (
                    <div className="multi-choice">
                        <PointDisplay points={points} />
                        <MultipleChoice
                            multiQuestion={currentSegment}
                            handleCorrect={handleCorrectAnswer}
                        />
                        <Box sx={{ width: "100%" }}>
                            <LinearProgress
                                variant="determinate"
                                value={progress}
                            />
                        </Box>
                    </div>
                )}
            </div>
        );
    } else {
        return <GoogleButton type="light" onClick={googleSignIn} />;
    }
}

export default App;
