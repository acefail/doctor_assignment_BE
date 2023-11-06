import express from "express";
import * as hospitalController from "../controllers/hospitalController.js";

const router = express.Router();

router.get("/", hospitalController.findAll);

export default router;