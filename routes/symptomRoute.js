import express from "express";
import * as symptomController from "../controllers/symptomController.js";

const router = express.Router();

router.get("/", symptomController.findAll);

export default router;