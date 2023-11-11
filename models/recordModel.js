import { model, Schema, Types } from 'mongoose';

export const COLLECTION_NAME = 'Medical_record';
export const DOCUMENT_NAME = 'MedicalRecord';

const MedicalRecordSchema = new Schema(
{
    // id: {
    //   type: Number,
    //   trim: true,
    //   unique: true,
    //   required: true,
    // },
    username: {
        type: String,
      unique: true,
      required: true,
    },
    hospital: {
        type: {
            type: Schema.Types.ObjectId,
            ref: "Hospital",
        },
    },
    symptoms: {
        type: [String],
        required: true,
    },
    create_at: {
      type: Date,
    },
},
  {
    timestamps: true,
  }
);

export const MedicalRecordModel = model(DOCUMENT_NAME, MedicalRecordSchema, COLLECTION_NAME);
