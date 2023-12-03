import appointmentRepo from "../db/repos/appointmentRepo.js";
import hospitalRepo from "../db/repos/hospitalRepo.js";
import userRepo from "../db/repos/userRepo.js";
const {
  createAppointment,
  findAllByPhoneNumber,
} = require("./appointmentController.js");

jest.mock("../db/repos/hospitalRepo", () => ({}));
jest.mock("../db/repos/userRepo", () => ({}));
jest.mock("../db/repos/appointmentRepo", () => ({}));

describe("findAllByPhoneNumber Endpoint", () => {
  it("should return user appointments with hospital details", async () => {
    // Mocking request body
    const mockRequestBody = {
      phoneNumber: "1234567890",
    };

    // Mocking the data returned by userRepo.findByPhoneNumber
    const mockUser = {
      phoneNumber: "1234567890",
      // Add other user properties as needed
    };
    userRepo.findByPhoneNumber = jest.fn().mockResolvedValue(mockUser);

    // Mocking the data returned by appointmentRepo.findByPhoneNumber
    const mockAppointments = [
      {
        hospitalId: 1,
        date: "2023-12-31",
        symptomsList: ["Symptom1", "Symptom2"],
        medicalRecord: "Medical record details",
      },
      // Add more mock appointments as needed
    ];
    appointmentRepo.findByPhoneNumber = jest
      .fn()
      .mockResolvedValue(mockAppointments);

    // Mocking the data returned by hospitalRepo.findById
    const mockHospital = {
      name: "Test Hospital",
      address: "123 Main St",
      // Add other hospital properties as needed
    };
    hospitalRepo.findById = jest.fn().mockResolvedValue(mockHospital);

    const mockRequest = { body: mockRequestBody };
    const mockResponse = {
      status: jest.fn(() => mockResponse),
      json: jest.fn(),
    };
    const mockNext = jest.fn();

    // Calling the findAllByPhoneNumber function
    await findAllByPhoneNumber(mockRequest, mockResponse, mockNext);

    // Checking that the response status is set to 200
    expect(mockResponse.status).toHaveBeenCalledWith(200);

    // Checking that the response JSON matches the expected structure
    expect(mockResponse.json).toHaveBeenCalledWith({
      result: [
        {
          hospitalName: "Test Hospital",
          hospitalAddress: "123 Main St",
          date: "2023-12-31",
          symptomsList: ["Symptom1", "Symptom2"],
          medicalRecord: "Medical record details",
        },
        // Add more expected result items as needed
      ],
    });
  });
});
