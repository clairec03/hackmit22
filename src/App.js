import { useState, useEffect } from "react";
import ReactPlayer from "react-player/youtube";

import getTimestamps from "./lib/firestore/getTimestamps";
import MultipleChoice from "./components/MultipleChoice";
import Box from "@mui/material/Box";
import LinearProgress from "@mui/material/LinearProgress";

import "./globals.css";

function App() {
    const [segments, setSegments] = useState([]); // segments are sorted
    const getSegmentsOnStart = async () => {
        setSegments(await getTimestamps("CSHistory"));
    };

    const [currentSegment, setCurrentSegment] = useState(null);

    const popupDelay = 20;
    const [seconds, setSeconds] = useState(0.0);

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

    const handleProgress = (secs) => {
        setSeconds(Math.floor(secs));
        if (
            currentSegment !== null &&
            seconds - currentSegment.seconds >= popupDelay
        ) {
            setCurrentSegment(null);
            setSegments(segments.slice(1)); // removes the first element
            setProgress(100);
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

    const vidUrl =
        "https://www.youtube.com/watch?v=Yocja_N5s1I&list=PLBDA2E52FB1EF80C9&index=1";

    const [progress, setProgress] = useState(100);

    useEffect(() => {
        const timer = setInterval(() => {
            setProgress((oldProgress) => {
                console.log(oldProgress);
                if (!currentSegment) {
                    return oldProgress;
                }
                // if (oldProgress === 0) {
                //     return 100;
                // }
                return Math.max(oldProgress - 1, 0);
            });
        }, popupDelay*9);
        return () => {
            clearInterval(timer);
        };
    }, [currentSegment]);

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
                    <MultipleChoice multiQuestion={currentSegment} />
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
}

export default App;
