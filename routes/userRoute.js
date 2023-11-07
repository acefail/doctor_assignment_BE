import express from "express";
import * as userController from "../controllers/userController.js";
import { verifyToken } from "../middlewares/authMiddleware.js";

const router = express.Router();

router.get("/", verifyToken, userController.findAll);
router.post("/login", userController.login)

export default router;