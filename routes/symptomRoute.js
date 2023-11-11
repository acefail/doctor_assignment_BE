import express from "express";
import * as symptomController from "../controllers/symptomController.js";
import { verifyToken } from "../middlewares/authMiddleware.js";

const router = express.Router();

router.get("/", verifyToken, symptomController.findAll);

export default router;