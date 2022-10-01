
import "./App.css";

import getQuestion from "./lib/firestore/getQuestion";


function printQuestion() {
    const qid = "x7Bm4AsanidDfi9WYEM9";
    const question = getQuestion(qid);
    console.log(question);
}

function App() {
    return (
        <div className="App">
            <button onClick={printQuestion}>
                Click me for question
            </button>
        </div>
    );
}

export default App;
