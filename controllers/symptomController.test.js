const { findAll } = require("./symptomController");

const symptomRepo = require("../db/repos/symptomRepo");

jest.mock("../db/repos/symptomRepo", () => ({}));

describe("findAll Endpoint", () => {
  it("should return a list of symptoms", async () => {
    // Mocking the data returned by symptomRepo.retrieveAll
    const mockSymptoms = [
      { id: 1, diseaseName: "Symptom 1" },
      { id: 2, diseaseName: "Symptom 2" },
      // Add more mock data as needed
    ];

    // Mocking the symptomRepo.retrieveAll function
    symptomRepo.retrieveAll = jest.fn().mockResolvedValue(mockSymptoms);

    const mockRequest = {};
    const mockResponse = {
      status: jest.fn(() => mockResponse),
      json: jest.fn(),
    };
    const mockNext = jest.fn();

    // Calling the findAll function
    await findAll(mockRequest, mockResponse, mockNext);

    // Checking that the response status is set to 200
    expect(mockResponse.status).toHaveBeenCalledWith(200);

    // Checking that the response JSON matches the expected structure
    expect(mockResponse.json).toHaveBeenCalledWith({
      messagse: mockSymptoms,
    });
  });
});
