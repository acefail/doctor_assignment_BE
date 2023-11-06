import { model, Schema, Types } from 'mongoose';

export const COLLECTION_NAME = 'Appointment';
export const DOCUMENT_NAME = 'Appointment';

const AppointmentSchema = new Schema(
{
    // id: {
    //   type: Number,
    //   trim: true,
    //   unique: true,
    //   required: true,
    // },
    date: {
        type: Date,
        
    },
    name: {
      type: String,
      unique: true,
      required: true,
    },
    slots: {
        type: Number,
        min: [0, "Must have greater or equal than 0 slots"],
        required: true,
    },
    phoneNumber: {
      type: String,
      required: true,
    },
    curableSymtomps: {
        type: [String],
    },
    address: {
        type: [Number],
        required: true,
    }
},
  {
    timestamps: true,
  }
);

export const AppointmentModel = model(DOCUMENT_NAME, AppointmentSchema, COLLECTION_NAME);
