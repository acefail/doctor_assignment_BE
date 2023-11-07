import express from "express";
import userRouter from "./userRoute.js"
import hospitalRouter from "./hospitalRoute.js"

const router = express.Router();
router.use("/api/user", userRouter);
router.use("/api/hospital", hospitalRouter);


export default router;