import { UserModel } from "../../models/userModel.js";

async function retrieveAll() {
    return UserModel.find({});
}


export default {
    retrieveAll,
}