import { setDoc, doc } from "firebase/firestore";

import { firestore } from "../firebase";

/**
 * Directly adds a profile with 0 points 'profiles' collection
 * @async Firestore add
 * @param {string} email
 * @throws null
 */
export default async function addUser(email) {
    const userRef = doc(firestore, "profiles", email);
    try {
        await setDoc(userRef, { points: 0 });
    } catch (err) {
        console.error("Error adding the profile documnet:", err);
    }
}
