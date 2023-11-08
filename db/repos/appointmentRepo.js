import { AppointmentModel } from "../../models/appointmentModel.js";

async function findByUsername(username) {
    return AppointmentModel.find({}).populate({
        path: "patient",
        match: {'username': username}
    }).exec();
}

export default {
    findByUsername,
}