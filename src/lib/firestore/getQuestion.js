import { getDoc, doc } from "firebase/firestore";

import { firestore } from "../firebase";


//! NOT WORKING RIGHT NOW

/**
 * Queries the "questions" collection by question ID
 * @async Firestore query
 * @param {string} lesson
 * @param {string} qid
 * @returns A promise containing the question document as an object
 * @throws null
 */
export default async function getQuestion(lesson, qid) {

    // const lessonRef = doc(firestore, "lessons", lesson, qid);
    // const segmentRef = doc(firestore, )

    // try {
    //     const docSnap = await getDoc(questionRef);
    //     if (docSnap.exists()) {
    //         return docSnap.data();
    //     } else {
    //         return null;
    //     }
    // } catch (err) {
    //     console.error("Error querying the user profile docuemnt", err);
    //     return null;
    // }
    return null;

}