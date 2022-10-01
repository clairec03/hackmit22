import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

import firebaseConfig from "../lib/firebaseConfig";

//* Initialize firebase
const firebaseApp = initializeApp(firebaseConfig);

//* Initialize auth and firestore with the 'firebaseApp' property
export const auth = getAuth(firebaseApp);
export const firestore = getFirestore(firebaseApp);

export default firebaseApp;