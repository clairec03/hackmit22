import { updateDoc, doc, increment } from "firebase/firestore";

import { firestore } from "../firebase";

/**
 * Adds a point to a user
 * @async Firestore add
 * @param {string} email
 * @throws null
 */
export default async function addPoint(email, points) {
    const userRef = doc(firestore, "profiles", email);
    try {
        await updateDoc(userRef, { points: increment(points) });
    } catch (err) {
        console.error("Error incrementing the points:", err);
    }
}
