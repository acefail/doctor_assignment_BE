import { model, Schema, Types } from 'mongoose';

export const COLLECTION_NAME = 'Symptom';
export const DOCUMENT_NAME = 'Symptom';

const SymptomSchema = new Schema(
{
    diseaseName: String
},
);

export const SymptomModel = model(DOCUMENT_NAME, SymptomSchema, COLLECTION_NAME);
