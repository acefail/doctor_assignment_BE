import userRepo from "../db/repos/userRepo.js";
import genToken from "../utils/genToken.js";

export const findAll = async (req, res, next) => {
  const users = await userRepo.retrieveAll();
  res.status(200).json({
    messagse: users,
  });
};

export const login = async (req, res, next) => {
  console.log("check login: ", req.body);
  const { phone, password } = req.body;
  if (!phone || !password) {
    res.status(400);
    return next(new Error("All fields must be filled"));
  }
  const user = await userRepo.findByPhoneNumber(phone);
  if (user && (user.password === password)) {
    res.status(200).json({
      result: user,
      token: genToken(user._id),
    });
  } else {
    res.status(400);
    return next(new Error("Invalid email or password"));
  }
};
