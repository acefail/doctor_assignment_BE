import { HospitalModel } from "../../models/hospitalModel.js";


async function retrieveAll() {
    return HospitalModel.find({});
}


export default {
    retrieveAll,
}