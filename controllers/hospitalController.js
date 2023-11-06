import hospitalRepo from "../db/repos/hospitalRepo.js";


export const findAll = async (req, res, next) => {
    const hospitals = await hospitalRepo.retrieveAll();
    res.status(200).json({
        messagse: hospitals,
    });
}