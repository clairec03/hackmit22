import React from "react";
import ReactDOM from "react-dom/client";
import { Toaster } from "react-hot-toast";
import App from "./App";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
    <React.StrictMode>
        <App />
        <Toaster
            toastOptions={{
                // Define default options
                duration: 4000,
                style: {
                    textAlign: "center",
                    borderRadius: "10px",
                },
                // Default options for specific types
                error: {
                    duration: 6000,
                },
            }}
        />
    </React.StrictMode>
);
