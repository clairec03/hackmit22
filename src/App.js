import "./App.css";
// import getQuestion from "./lib/firestore/getQuestion";

// import React from 'react'
import ReactPlayer from 'react-player/youtube'


const vidUrl = "https://www.youtube.com/watch?v=Yocja_N5s1I&list=PLBDA2E52FB1EF80C9&index=1";


function App() {
    return (
        <div className="App">
            <ReactPlayer url={vidUrl} />
        </div>
    );
}

export default App;



/* <button onClick={printQuestion}>Click me for question</button> */
