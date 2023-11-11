import appointmentRepo from "../db/repos/appointmentRepo.js";
import userRepo from "../db/repos/userRepo.js";

export const findAllByUsername = async (req, res, next) => {
  const { username } = req.params;
  const user = await userRepo.findByUsername(username);
  if (!user) {
    res.status(400).json({
      message: "User doesn't exist",
    });
    return;
  }
  const appointments = await appointmentRepo.findByUsername(user.username);
  res.status(200).json({
    message: appointments,
  });
};

export const createAppointment = async (req, res, next) => {
  try {
    const { hospitalId, patientPhoneNumber, date } = req.body;
    const appointment = await appointmentRepo.createAppointment({
      date: date,
      hospital: hospitalId,
      patientPhoneNumber: patientPhoneNumber,
      symptomsList: [],
      address: null,
    });
    res.status(200).json(appointment).end();
  } catch (error) {
    console.log(error);
    return res.sendStatus(400);
  }
};

export const findAllByPhoneNumber = async (req, res, next) => {
  const { fullName, phoneNumber, dob, date, symptomsList, address } = req.body;
  const user = await userRepo.findByPhoneNumber(phoneNumber);
  if (!user) {
    res.status(400).json({
      message: "User doesn't exist",
    });
    return;
  }
  const appointments = await appointmentRepo.findByPhoneNumber(user.phoneNumber);
  res.status(200).json({
    message: appointments,
  });
};
