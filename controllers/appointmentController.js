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
    const { hospital, createdAt } = req.body;
    const appointment = await appointmentRepo.createAppointment({
      date: createdAt,
      hospital: hospital,
      patient: null,
      symptomsList: [],
      address: null,
    });
    res.status(200).json(appointment).end();
  } catch (error) {
    console.log(error);
    return res.sendStatus(400);
  }
};
