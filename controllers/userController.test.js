const { findAll, findInfoByUsername } = require("./userController");
const userRepo = require("../db/repos/userRepo");
const { UserModel } = require("../models/userModel");

jest.mock("../db/repos/userRepo", () => ({}));

describe("findAll Endpoint", () => {
  it("should return a list of users", async () => {
    // Giả lập một số dữ liệu
    const mockUserData = {
      gender: "Male",
      address: [123, 456],
      password: "securepassword",
      name: "John Doe",
      dob: new Date("1990-01-01"),
      phoneNumber: "1234567890",
      records: [],
    };

    // Mock hàm find của UserModel để trả về dữ liệu giả lập
    userRepo.retrieveAll = jest.fn().mockResolvedValue(mockUserData);

    const mockRequest = {};
    const mockResponse = {
      status: jest.fn(() => mockResponse),
      json: jest.fn(),
    };
    const mockNext = jest.fn();

    // Gọi hàm kiểm tra
    await findAll(mockRequest, mockResponse, mockNext);

    // Kiểm tra rằng response có status 200 (OK)
    expect(mockResponse.status).toHaveBeenCalledWith(200);

    // Kiểm tra rằng response chứa thông điệp và là một mảng người dùng
    expect(mockResponse.json).toHaveBeenCalledWith({
      messagse: {
        address: [123, 456],
        dob: new Date("1990-01-01T00:00:00.000Z"),
        gender: "Male",
        name: "John Doe",
        password: "securepassword",
        phoneNumber: "1234567890",
        records: [],
      },
    });

    // Làm sạch mock sau khi kiểm tra
    userRepo.retrieveAll.mockRestore();
  }, 5000); // Timeout là 10 giây
});

describe("findInfoByUsername Endpoint", () => {
  it("should return user information when user is found", async () => {
    // Giả lập người dùng tồn tại
    const mockUser = {
      phoneNumber: "1234567890",
      name: "John Doe",
    };

    // Mock hàm findByPhoneNumber của userRepo
    userRepo.findByPhoneNumber = jest.fn().mockResolvedValue(mockUser);

    const mockRequest = {
      params: {
        phoneNumber: "1234567890",
      },
    };
    const mockResponse = {
      status: jest.fn(() => mockResponse),
      json: jest.fn(),
    };
    const mockNext = jest.fn();

    // Gọi hàm kiểm tra
    await findInfoByUsername(mockRequest, mockResponse, mockNext);

    // Kiểm tra rằng response có status 200 (OK)
    expect(mockResponse.status).toHaveBeenCalledWith(200);

    // Kiểm tra rằng response chứa thông điệp và là đối tượng người dùng
    expect(mockResponse.json).toHaveBeenCalledWith({
      message: mockUser,
    });

    // Làm sạch mock sau khi kiểm tra
    userRepo.findByPhoneNumber.mockRestore();
  }, 5000);

  it("should return an error message when user is not found", async () => {
    // Giả lập người dùng không tồn tại
    const mockUser = null;

    // Mock hàm findByPhoneNumber của userRepo
    userRepo.findByPhoneNumber = jest.fn().mockResolvedValue(mockUser);

    const mockRequest = {
      params: {
        phoneNumber: "1234567890",
      },
    };
    const mockResponse = {
      status: jest.fn(() => mockResponse),
      json: jest.fn(),
    };
    const mockNext = jest.fn();

    // Gọi hàm kiểm tra
    await findInfoByUsername(mockRequest, mockResponse, mockNext);

    // Kiểm tra rằng response có status 400 (Bad Request)
    expect(mockResponse.status).toHaveBeenCalledWith(400);

    // Kiểm tra rằng response chứa thông điệp
    expect(mockResponse.json).toHaveBeenCalledWith({
      message: "User doesn't exist",
    });

    // Làm sạch mock sau khi kiểm tra
    userRepo.findByPhoneNumber.mockRestore();
  }, 5000);
});
