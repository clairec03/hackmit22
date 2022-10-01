import { useState } from "react";
import ReactPlayer from "react-player/youtube";

import getTimestamps from "./lib/firestore/getTimestamps";
import MultipleChoice from "./components/MultipleChoice";
// import RadioForm from "./components/RadioForm";

import "./globals.css";

function App() {
    const [segments, setSegments] = useState([]); // segments are sorted
    const getSegmentsOnStart = async () => {
        setSegments(await getTimestamps("CSHistory"));
    };

    const [currentSegment, setCurrentSegment] = useState(null);

    const popupDelay = 3;
    const [seconds, setSeconds] = useState(0.0);

    const randomizeSetCurrentSegment = (sg) => {
        let answers = sg.options.slice();
        answers.push(sg.answer.slice());
        for (let i = 3; i > 0; i--) { // Fischer-Yates shuffle
            let j = Math.floor(Math.random() * (i + 1));
            let tmp = answers[i];
            answers[i] = answers[j];
            answers[j] = tmp;
        }
        console.log(answers);
        setCurrentSegment({
            options: answers.slice(), // pushes answer into the options and randomizes
            ...sg,
        });
    }

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
                    randomizeSetCurrentSegment(segments[i]);
                    
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
                width="75vw"
                height="75vh"
                onProgress={(e) => handleProgress(e.playedSeconds)}
                onStart={getSegmentsOnStart}
            />
            {currentSegment && <div>
                <MultipleChoice multiQuestion={currentSegment}/>
            </div>}
            
        </div>
    );
}

export default App;
