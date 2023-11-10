import express from "express";
import * as appointmentController from "../controllers/appointmentController.js";

const router = express.Router();

router.get("/:username", appointmentController.findAllByUsername);
router.get("/createappointment", appointmentController.createAppointment);

export default router;
