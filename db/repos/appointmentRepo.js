import { AppointmentModel } from "../../models/appointmentModel.js";

async function findByUsername(username) {
  return AppointmentModel.find({})
    .populate({
      path: "patient",
      match: { username: username },
    })
    .exec();
}

async function findByPhoneNumber(patientPhoneNumber) {
  return AppointmentModel.find({patientPhoneNumber: patientPhoneNumber});
}

async function createAppointment(Appointment) {
  return AppointmentModel.create(Appointment);
}

export default {
  findByUsername,
  createAppointment,
  findByPhoneNumber
};
