import { getStorage, ref } from "firebase/storage";

const storageObj = getStorage();
//* Root reference to storage
export const storage = ref(storageObj);