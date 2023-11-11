import express from "express";
import * as appointmentController from "../controllers/appointmentController.js";
import { verifyToken } from "../middlewares/authMiddleware.js";

const router = express.Router();

// router.get("/:username", appointmentController.findAllByUsername);
router.get("/", verifyToken, appointmentController.findAllByPhoneNumber);
router.post("/create-appointment", verifyToken, appointmentController.createAppointment);

export default router;
