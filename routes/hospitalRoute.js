import express from "express";
import * as hospitalController from "../controllers/hospitalController.js";

const router = express.Router();

router.get("/", hospitalController.findAll);
router.get("/recommend", hospitalController.getRecommendedList);

export default router;