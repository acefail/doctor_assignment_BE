import { UserModel } from "../../models/userModel.js";

async function retrieveAll() {
	return UserModel.find({});
}

async function findByPhoneNumber(phoneNumber) {
	return UserModel.findOne({ 'phone': phoneNumber });
}

async function createUser(User) {
	return UserModel.create(User);
}

export default {
	retrieveAll,
	findByPhoneNumber,
	createUser
}