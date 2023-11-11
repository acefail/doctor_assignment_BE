import { HospitalModel } from "../../models/hospitalModel.js";


async function retrieveAll() {
    return HospitalModel.find({});
}

async function getRecommendedList(req) {
    const hospitals = await retrieveAll();
    const suitables =  hospitals.filter((hos) => req.symptomsList.every(v => hos.Curable_symptom_list.includes(v)) && hos.slots > 0);
    if (suitables.length > 1) {
        suitables.sort((a,b) => {
            if (Math.abs((a.address[0]-req.address[0])*(a.address[0]-req.address[0]) + (a.address[1]-req.address[1])*(a.address[1]-req.address[1])) > Math.abs((b.address[0]-req.address[0])*(b.address[0]-req.address[0]) + (b.address[1]-req.address[1])*(b.address[1]-req.address[1]))) {
                return 1;
            } else if (Math.abs((a.address[0]-req.address[0])*(a.address[0]-req.address[0]) + (a.address[1]-req.address[1])*(a.address[1]-req.address[1])) < Math.abs((b.address[0]-req.address[0])*(b.address[0]-req.address[0]) + (b.address[1]-req.address[1])*(b.address[1]-req.address[1]))) {
                return -1;
            }
            return 0;
        })
    }
    return suitables
}

async function findById(hospitalId) {
    return HospitalModel.findOne({'id': hospitalId});
  }

export default {
    retrieveAll,
    getRecommendedList,
    findById
}