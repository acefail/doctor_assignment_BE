import express from "express";
import dotenv from "dotenv";
import bodyParser from "body-parser";
import { notFound, errorHandler } from "./middlewares/errorMiddleware.js";
import conn from "./db/index.js";
import cors from "cors";
import router from "./routes/index.js"

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// --------------------------DEPLOYMENT-----------------------
// let __dirname1 = path.resolve();
// __dirname1 = __dirname1.substring(0, __dirname1.length - 7)
// console.log(__dirname1)

// if (process.env.NODE_ENV === "production") {
//     app.use(express.static(path.join(__dirname1, "/client/build")));

//     app.get("*", (req, res) =>
//       res.sendFile(path.resolve(__dirname1, "client", "build", "index.html"))
//     );
//   } else {
//     app.get("/", (req, res) => {
//       res.send("API BKMotel is running..");
//     });
// }
// --------------------------DEPLOYMENT-----------------------
app.use(cors());
conn();


app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});
//   })
//   .catch((error) => console.log(`Server can't listening`));

app.use('/', router);
app.use(notFound);
app.use(errorHandler);