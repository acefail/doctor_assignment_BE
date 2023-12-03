const { findAll, getRecommendedList } = require("./hospitalController");
const hospitalRepo = require("../db/repos/hospitalRepo");

jest.mock("../db/repos/hospitalRepo", () => ({}));

describe("findAll Endpoint", () => {
  it("should return a list of hospitals", async () => {
    // Mocking the data returned by hospitalRepo.retrieveAll
    const mockHospitals = [
      {
        id: 1,
        name: "Hospital 1",
        slots: 10,
        phone: "1234567890",
        Curable_symptom_list: ["Symptom1"],
        address: [123, 456],
      },
      {
        id: 2,
        name: "Hospital 2",
        slots: 15,
        phone: "9876543210",
        Curable_symptom_list: ["Symptom2"],
        address: [789, 321],
      },
    ];

    // Mocking the hospitalRepo.retrieveAll function
    hospitalRepo.retrieveAll = jest.fn().mockResolvedValue(mockHospitals);

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
      messagse: mockHospitals,
    });
  });
});

describe("getRecommendedList Endpoint", () => {
  it("should return a list of recommended hospitals", async () => {
    // Mocking request body
    const mockRequestBody = {
      address: [123, 456],
      symptoms: ["Symptom1", "Symptom2"],
    };

    // Mocking the data returned by hospitalRepo.getRecommendedList
    const mockRecommendedList = [
      {
        id: 1,
        name: "Hospital 1",
        slots: 10,
        phone: "1234567890",
        Curable_symptom_list: ["Symptom1"],
        address: [123, 456],
      },
      {
        id: 2,
        name: "Hospital 2",
        slots: 15,
        phone: "9876543210",
        Curable_symptom_list: ["Symptom2"],
        address: [789, 321],
      },
      // Add more mock data as needed
    ];

    // Mocking the hospitalRepo.getRecommendedList function
    hospitalRepo.getRecommendedList = jest
      .fn()
      .mockResolvedValue(mockRecommendedList);

    const mockRequest = { body: mockRequestBody };
    const mockResponse = {
      status: jest.fn(() => mockResponse),
      json: jest.fn(),
    };
    const mockNext = jest.fn();

    // Calling the getRecommendedList function
    await getRecommendedList(mockRequest, mockResponse, mockNext);

    // Checking that the response status is set to 200
    expect(mockResponse.status).toHaveBeenCalledWith(200);

    // Checking that the response JSON matches the expected structure
    expect(mockResponse.json).toHaveBeenCalledWith({
      messagse: mockRecommendedList,
    });
  });
});
