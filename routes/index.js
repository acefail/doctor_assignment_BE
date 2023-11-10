import express from "express";
import userRouter from "./userRoute.js"
import hospitalRouter from "./hospitalRoute.js"
import appointmentRouter from "./appointmentRoute.js"
import symptomRoute from "./symptomRoute.js"

const router = express.Router();
router.use("/api/user", userRouter);
router.use("/api/hospital", hospitalRouter);
router.use("/api/appointment", appointmentRouter);
router.use("/api/symptom", symptomRoute)


export default router;