import "./App.css";

import getQuestion from "./lib/firestore/getQuestion";
import Video from "./components/Video";


async function printQuestion() {
    const qid = "x7Bm4AsanidDfi9WYEM9";
    const question = await getQuestion(qid);
    console.log(question);
}

const videoSrc = "https://ik.imagekit.io/cjtsui/videodemo/o/videos%2Fshorts%2Fmixkit-small-flowering-plants-in-a-nursery-43709.mp4?tr=w-500&alt=media&token=8ccfe3b8-6b33-40da-ae06-b02275f9749f";



function App() {
    return (
        <div className="App">
            <button onClick={printQuestion}>Click me for question</button>
            <Video src={videoSrc}/>
        </div>
    );
}

export default App;
