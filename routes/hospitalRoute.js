import express from "express";
import * as hospitalController from "../controllers/hospitalController.js";
import { verifyToken } from "../middlewares/authMiddleware.js";

const router = express.Router();

router.get("/", verifyToken, hospitalController.findAll);
router.post("/recommend", verifyToken, hospitalController.getRecommendedList);

export default router;