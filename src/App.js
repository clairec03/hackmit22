import { useState } from "react";
import ReactPlayer from "react-player/youtube";

import getTimestamps from "./lib/firestore/getTimestamps";

function App() {
    
    const [seconds, setSeconds] = useState(0.0);
    const handleProgress = (secs) => {
        setSeconds(Math.floor(secs));
    };
    
    const [segments, setSegments] = useState(null);
    const getSegmentsOnStart = async () => {
        setSegments(await getTimestamps("CSHistory"));
    };


    const vidUrl =
        "https://www.youtube.com/watch?v=Yocja_N5s1I&list=PLBDA2E52FB1EF80C9&index=1";

    return (
        <div className="App">
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

