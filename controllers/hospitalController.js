import hospitalRepo from "../db/repos/hospitalRepo.js";
import { RecommendedHospitalRequest } from "../models/core/requests.js";


export const findAll = async (req, res, next) => {
    const hospitals = await hospitalRepo.retrieveAll();
    res.status(200).json({
        messagse: hospitals,
    });
}

export const getRecommendedList = async (req, res, next) => {
    const {address, symptoms} = req.body
    const recListRequest = new RecommendedHospitalRequest(address, symptoms)
    const suitables = await hospitalRepo.getRecommendedList(recListRequest)
    res.status(200).json({
        messagse: suitables
    }) 
}