import { collection, getDocs } from "firebase/firestore";

import { firestore } from "../firebase";

/**
 * Retrieves all the timestamps of segments in seconds
 * @async Firestore query
 * @param {string} lesson
 * @returns An array of numbers
 * @throws null
 */
export default async function getTimestamps(lesson) {
    let questions = []
    const querySnapshot = await getDocs(collection(firestore, lesson));
    querySnapshot.forEach((doc) => {
        // console.log(doc.id, " => ", doc.data());
        const segment = {
            seconds: Number(doc.id),
            ...doc.data(),
        }
        questions.push(segment);
    });
    return questions;
    
}
