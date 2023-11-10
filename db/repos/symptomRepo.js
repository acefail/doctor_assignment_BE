import { SymptomModel } from "../../models/symptomModel.js";

async function retrieveAll() {
    return SymptomModel.find({});
}

export default {
    retrieveAll
}