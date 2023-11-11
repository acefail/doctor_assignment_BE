import userRepo from "../db/repos/userRepo.js";
import genToken from "../utils/genToken.js";
// import { random, authentication } from "../helpers/authenticate.js";
import bcrypt from "bcrypt";

export const findAll = async (req, res, next) => {
  const users = await userRepo.retrieveAll();
  res.status(200).json({
    messagse: users,
  });
};

export const findInfoByUsername = async (req, res, next) => {
  const { phoneNumber } = req.params;
  const user = await userRepo.findByPhoneNumber(phoneNumber);
  if (!user) {
    res.status(400).json({
      message: "User doesn't exist",
    });
    return;
  }
  res.status(200).json({
    message: user,
  });
};

export const signup = async (req, res, next) => {
  console.log("check signup: ", req.body);
  try {
    const { gender, phone, password, fullName, dob } = req.body;
    if (!phone || !password || !fullName || !dob || !gender) {
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
  const { phoneNumber, password } = req.body;
  if (!phoneNumber || !password) {
    res.status(400);
    return next(new Error("All fields must be filled"));
  }
  const user = await userRepo.findByPhoneNumber(phoneNumber);
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

// Cập nhật thông tin người dùng
export const updateInfo = async (req, res, next) => {
  try {
    const { phoneNumber } = req.params;
    const { gender, phone, password, fullName, address, dob } = req.body
    var user = await userRepo.findByPhoneNumber(phoneNumber);
    if (!user) {
      res.status(400).json({
        message: "User doesn't exist",
      });
      return;
    }

    const salt = await bcrypt.genSalt(10);
    const hashPassword = await bcrypt.hash(password, salt);

    const updatedUser = await userRepo.updateUser({
      phoneNumber: phone,
      name: fullName,
      address: address,
      dob: dob,
      gender: gender,
      password: hashPassword
    });

    res.status(200).json({
      message: "Update successful!",
    });
  } catch (error) {
    console.log(error);
    return res.sendStatus(400);
  }
};