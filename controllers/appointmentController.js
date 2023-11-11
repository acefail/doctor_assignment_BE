import appointmentRepo from "../db/repos/appointmentRepo.js";
import hospitalRepo from "../db/repos/hospitalRepo.js";
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
    const { hospitalId, patientPhoneNumber, date, symptomsList } = req.body;
    const appointment = await appointmentRepo.createAppointment({
      date: date,
      hospitalId: hospitalId,
      patientPhoneNumber: patientPhoneNumber,
      symptomsList: symptomsList,
      address: null,
    });
    res.status(200).json(appointment).end();
  } catch (error) {
    console.log(error);
    return res.sendStatus(400);
  }
};

export const findAllByPhoneNumber = async (req, res, next) => {
  const { phoneNumber } = req.body;
  const user = await userRepo.findByPhoneNumber(phoneNumber);
  if (!user) {
    res.status(400).json({
      message: "User doesn't exist",
    });
    return;
  }
  const appointments = await appointmentRepo.findByPhoneNumber(user.phoneNumber);
  
  var result = await Promise.all(appointments.map( async (appointment)=>{
    const hospital = await hospitalRepo.findById(appointment.hospitalId);
    const resItem = {
      hospitalName: hospital.name,
      hospitalAddress: hospital.address,
      date: appointment.date,
      symptomsList: appointment.symptomsList,
    }
    return resItem;
  })) 

  res.status(200).json({
    result: result,
  });
};
