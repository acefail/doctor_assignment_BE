import { UserModel } from "../../models/userModel.js";

async function retrieveAll() {
    return UserModel.find({});
}

async function findByUsername(username) {
    return UserModel.findOne({username: username})
} 


export default {
    retrieveAll,
    findByUsername,
}