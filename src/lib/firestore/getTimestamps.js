import { collection, getDocs } from "firebase/firestore";

import { firestore } from "../firebase";

/**
 * Retrieves all the timestamps of segments in seconds
 * @async Firestore query
 * @param {string} lesson
 * @returns An array of objects, each object representing a question
 * @throws null
 */
export default async function getTimestamps(lesson) {
    let questions = [];
    const lessonSnapshot = await getDocs(collection(firestore, lesson));
    lessonSnapshot.forEach((doc) => {
        // console.log(doc.id, " => ", doc.data());
        const segment = {
            seconds: Number(doc.id),
            ...doc.data(),
        };
        questions.push(segment);
    });
    questions.sort((a, b) => {
        return a.seconds < b.seconds ? -1 : a.seconds > b.seconds ? 1 : 0;
    });
    return questions;
}
