import { UserModel } from "../../models/userModel.js";

async function retrieveAll() {
    return UserModel.find({});
}

async function findByUsername(username) {
    return UserModel.findOne({'username': username})
} 
async function findByPhoneNumber(phoneNumber) {
    return UserModel.findOne({'phone': phoneNumber})
}


export default {
    retrieveAll,
    findByUsername,
    findByPhoneNumber,
}