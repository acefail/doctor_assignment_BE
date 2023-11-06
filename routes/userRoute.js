import express from "express";
import * as userController from "../controllers/userController.js";

const router = express.Router();

router.get("/", userController.findAll);
router.get("/hi", userController.sayHi);

export default router;