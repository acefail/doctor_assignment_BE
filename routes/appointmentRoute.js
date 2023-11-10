import express from "express";
import * as appointmentController from "../controllers/appointmentController.js";

const router = express.Router();

// router.get("/:username", appointmentController.findAllByUsername);
router.get("/:phoneNumber", appointmentController.findAllByPhoneNumber);
router.post("/create-appointment", appointmentController.createAppointment);

export default router;
