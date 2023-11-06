import userRepo from "../db/repos/userRepo.js";

export const sayHi = async (req, res, next) => {
    res.status(200).json({
        messagse: "Hello",
    });
}

export const findAll = async (req, res, next) => {
    const users = await userRepo.retrieveAll();
    res.status(200).json({
        messagse: users,
    });
}