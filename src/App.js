import logo from "./logo.svg";
import "./App.css";

function App() {
    return (
        <div className="App">
            {/* <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                    Edit <code>src/App.js</code> and save to reload.
                </p>
                <a
                    className="App-link"
                    href="https://reactjs.org"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Learn React
                </a>
            </header> */}
            <video>
                <source src="https://firebasestorage.googleapis.com/v0/b/hackmit22.appspot.com/o/videos%2Fshorts%2Fmixkit-small-flowering-plants-in-a-nursery-43709.mp4?alt=media&token=8ccfe3b8-6b33-40da-ae06-b02275f9749f" type="video/mp4" />
            </video>
        </div>
    );
}

export default App;
