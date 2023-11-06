import mongoose from "mongoose";

const options = {
    autoIndex: true,
    connectTimeoutMS: 60000, // Give up initial connection after 10 seconds
    socketTimeoutMS: 45000, // Close sockets after 45 seconds of inactivity
};

function setRunValidators() {
  this.setOptions({ runValidators: true });
}

mongoose.set('strictQuery', true);

const conn = async () => {
  try {
    const conn = await mongoose
      .set("strictQuery", true)
      .connect(process.env.DB_CONNECT, options);
    console.log("Successfully connected to database");
  } catch (error) {
    console.log(`Error: ${error.message}`);
    process.exit();
  }
};

export default conn;