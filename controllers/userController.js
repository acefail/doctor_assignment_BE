import userRepo from "../db/repos/userRepo.js";
import genToken from "../utils/genToken.js";
import { random, authentication } from "../helpers/authenticate.js";
import bcrypt from 'bcrypt'

export const findAll = async (req, res, next) => {
	const users = await userRepo.retrieveAll();
	res.status(200).json({
		messagse: users,
	});
};

export const signup = async (req, res, next) => {
	console.log("check signup: ", req.body);
	try {
		const { gender, phone, password, fullName, address, dob } = req.body;
		if (!phone || !password || !fullName || !address || !dob || !gender) {
			res.status(400);
			return next(new Error("All fields must be filled"));
		}

		const existingUser = await userRepo.findByPhoneNumber(phone);
		if (existingUser) {
			res.status(400);
			return next(new Error("User already existed!"));
		}

		const salt = await bcrypt.genSalt(10);
		const hashPassword = await bcrypt.hash(password, salt);
		const user = await userRepo.createUser({
			phoneNumber: phone,
			password: hashPassword,
			name: fullName,
			gender: gender,
			dob: dob,
			address: address,
			records: [],
		});

		res.status(200).json(user).end();
	} catch (error) {
		console.log(error);
		return res.sendStatus(400);
	}
};

export const login = async (req, res, next) => {
	console.log("check login: ", req.body);
	const { phone, password } = req.body;
	if (!phone || !password) {
		res.status(400);
		return next(new Error("All fields must be filled"));
	}
	const user = await userRepo.findByPhoneNumber(phone);
	if (user) {
		const checkPassword = await bcrypt.compare(password, user.password);
		if (!checkPassword) {
			res.status(400);
			return next(new Error("Incorrect password"));
		}
		res.status(200).json({
			result: user,
			token: genToken(user._id),
		});
	} else {
		res.status(400);
		return next(new Error("Cannot find user with the phone number"));
	}
};
