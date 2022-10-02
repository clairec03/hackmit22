import { setDoc, doc } from "firebase/firestore";

import { firestore } from "../firebase";




async function addAllSegments(segmentJson) {
    const segmentList = [];
    for (let i = 0; i < segmentList.length; i++) {
        addTimestamp(segmentList[i]);
    }
}



/**
 * Adds a timestamp/segment to a lesson
 * @async Firestore create a timestamp in a lesson
 * @throws "" (Empty String)
 */
export default async function addTimestamp(segment) {

    const timestamp = doc(firestore, segment.seconds);

    const newStudent = {
        question: segment.question,
        answer: segment.answer,
        options: segment.options,
    };

    try {
       await setDoc(timestamp, newStudent);
    } catch (err) {
        console.error("Error creating a new student:", err);
    }

}
