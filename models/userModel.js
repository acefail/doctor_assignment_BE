import { model, Schema, Types } from "mongoose";

export const COLLECTION_NAME = "User";
export const DOCUMENT_NAME = "User";

const UserSchema = new Schema({
	// id: {
	//   type: Number,
	//   trim: true,
	//   unique: true,
	//   required: true,
	// },
	// username: {
	// 	type: String,
	// 	unique: true,
	// },
	gender: {
		type: String,
		required: true,
	},
	address: {
		type: [ Number ],
		required: true,
	},
	password: {
		type: String,
		minLength: 8,
		required: true,
	},
	name: {
		type: String,
		required: true,
	},
	dob: {
		type: Date,
		required: true,
	},
	phoneNumber: {
		type: String,
		required: true,
	},
	records: {
		type: [
			{
				type: Schema.Types.ObjectId,
				ref: "MedicalRecord",
			},
		],
	},
});

export const UserModel = model(DOCUMENT_NAME, UserSchema, COLLECTION_NAME);
