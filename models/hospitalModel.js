import { model, Schema, Types } from 'mongoose';

export const COLLECTION_NAME = 'Hospital';
export const DOCUMENT_NAME = 'Hospital';

const HospitalSchema = new Schema(
{
    // id: {
    //   type: Number,
    //   trim: true,
    //   unique: true,
    //   required: true,
    // },
    id: {
      type: Number,
      unique: true
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
    phone: {
      type: String,
      required: true,
    },
    Curable_symptom_list: {
        type: [String],
    },
    address: {
        type: [Number],
        required: true,
    }
},
);

export const HospitalModel = model(DOCUMENT_NAME, HospitalSchema, COLLECTION_NAME);
