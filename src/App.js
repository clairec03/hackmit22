import { useState } from "react";
import ReactPlayer from "react-player/youtube";

import getTimestamps from "./lib/firestore/getTimestamps";

import "./globals.css";

function App() {
    const [segments, setSegments] = useState([]); // segments are sorted
    const getSegmentsOnStart = async () => {
        setSegments(await getTimestamps("CSHistory"));
    };

    const [currentSegment, setCurrentSegment] = useState(null);

    const popupDelay = 20;
    const [seconds, setSeconds] = useState(0.0);
    const handleProgress = (secs) => {
        setSeconds(Math.floor(secs));
        if (currentSegment !== null &&
                seconds - currentSegment.seconds >= popupDelay) {
            setCurrentSegment(null);
            setSegments(segments.shift()) // removes the first element
            return;
        }
        if (currentSegment === null) {
            for (let i = 0; i < segments.length; i++) {
                if (segments[i].seconds <= seconds) {
                    setCurrentSegment(segments[i]);
                }
            }
        }
    };

    const vidUrl =
        "https://www.youtube.com/watch?v=Yocja_N5s1I&list=PLBDA2E52FB1EF80C9&index=1";

    return (
        <div className="center">
            <ReactPlayer
                url={vidUrl}
                playing={true}
                volume={1}
                width="70vw"
                height="70vh"
                onProgress={(e) => handleProgress(e.playedSeconds)}
                onStart={getSegmentsOnStart}
            />
        </div>
    );
}

export default App;
