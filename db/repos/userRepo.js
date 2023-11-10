import { UserModel } from "../../models/userModel.js";

async function retrieveAll() {
	return UserModel.find({});
}
async function findByUsername(username) {
	return UserModel.findOne({ 'username': username })
}

async function findByPhoneNumber(phoneNumber) {
	return UserModel.findOne({ 'phoneNumber': phoneNumber });
}

async function createUser(User) {
	return UserModel.create(User);
}

async function updateUser(User) {
	return UserModel.updateOne({ 'phoneNumber': User.phoneNumber }, {
		phoneNumber: User.phoneNumber,
		name: User.name,
		address: User.address,
		dob: User.dob,
		gender: User.gender,
		password: User.password
	})
}

export default {
	retrieveAll,
	findByPhoneNumber,
	findByUsername,
	createUser,
	updateUser
}