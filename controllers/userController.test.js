const {
  findAll,
  findInfoByUsername,
  signup,
  login,
  updateInfo,
} = require("./userController");
const userRepo = require("../db/repos/userRepo");
const { UserModel } = require("../models/userModel");
const bcrypt = require("bcrypt");

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

// Mocking bcrypt functions
jest.mock("bcrypt");
const mockGenSalt = jest.fn();
const mockHash = jest.fn();
bcrypt.genSalt = mockGenSalt;
bcrypt.hash = mockHash;

describe("signup Endpoint", () => {
  let mockRequest;
  let mockResponse;
  let mockNext;

  beforeEach(() => {
    mockRequest = {
      body: {
        gender: "Male",
        phone: "1234567890",
        password: "securepassword",
        fullName: "John Doe",
        dob: new Date("1990-01-01"),
      },
    };
    mockResponse = {
      status: jest.fn(() => mockResponse),
      json: jest.fn(),
      sendStatus: jest.fn(),
    };
    mockNext = jest.fn();
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  it("should create a new user and return it when all fields are provided and user does not exist", async () => {
    // Mocking userRepo.findByPhoneNumber to simulate a non-existing user
    userRepo.findByPhoneNumber.mockResolvedValue(null);

    // Mocking bcrypt functions
    mockGenSalt.mockResolvedValue("mockedSalt");
    mockHash.mockResolvedValue("mockedHash");

    // Mocking userRepo.createUser to simulate user creation
    const mockCreatedUser = {
      phoneNumber: "1234567890",
      password: "mockedHash",
      name: "John Doe",
      gender: "Male",
      dob: new Date("1990-01-01"),
      records: [],
    };
    userRepo.createUser = jest.fn().mockResolvedValue(mockCreatedUser);

    await signup(mockRequest, mockResponse, mockNext);

    // Assert that the user was created and returned in the response
    expect(mockResponse.status).toHaveBeenCalledWith(200);
    expect(mockResponse.json).toHaveBeenCalledWith(mockCreatedUser);
    expect(mockNext).not.toHaveBeenCalled();
  });

  it("should return an error when any field is missing", async () => {
    // Remove one required field from the request
    delete mockRequest.body.fullName;

    await signup(mockRequest, mockResponse, mockNext);

    // Assert that the response status is 400 and an error is sent to next middleware
    expect(mockResponse.status).toHaveBeenCalledWith(400);
    expect(mockNext).toHaveBeenCalledWith(expect.any(Error));
    expect(mockResponse.json).not.toHaveBeenCalled();
  });

  it("should return an error when the user already exists", async () => {
    // Mocking userRepo.findByPhoneNumber to simulate an existing user
    userRepo.findByPhoneNumber.mockResolvedValue({});

    await signup(mockRequest, mockResponse, mockNext);

    // Assert that the response status is 400 and an error is sent to next middleware
    expect(mockResponse.status).toHaveBeenCalledWith(400);
    expect(mockNext).toHaveBeenCalledWith(expect.any(Error));
    expect(mockResponse.json).not.toHaveBeenCalled();
  });
});

// Mocking bcrypt functions
jest.mock("bcrypt");
const mockCompare = jest.fn();
bcrypt.compare = mockCompare;

// Mocking genToken function
jest.mock("../utils/genToken.js");
const { genToken } = require("../utils/genToken.js");
import jwt from "jsonwebtoken";

describe("login Endpoint", () => {
  let mockRequest;
  let mockResponse;
  let mockNext;

  beforeEach(() => {
    mockRequest = {
      body: {
        phoneNumber: "1234567890",
        password: "securepassword",
      },
    };
    mockResponse = {
      status: jest.fn(() => mockResponse),
      json: jest.fn(),
    };
    mockNext = jest.fn();
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  it("should successfully log in and return user information and token", async () => {
    // Mocking userRepo.findByPhoneNumber to simulate an existing user
    const mockUser = {
      _id: "mockUserId",
      phoneNumber: "1234567890",
      password: "hashedPassword",
    };
    userRepo.findByPhoneNumber.mockResolvedValue(mockUser);

    // Mocking bcrypt.compare to simulate a successful password check
    mockCompare.mockResolvedValue(true);

    // Mocking genToken function
    const mockToken = "mockToken";
    jest.spyOn(jwt, "sign").mockReturnValue(mockToken);

    await login(mockRequest, mockResponse, mockNext);

    // Assert that the response status is 200 and contains user information and token
    expect(mockResponse.status).toHaveBeenCalledWith(200);

    expect(mockNext).not.toHaveBeenCalled();
  });

  it("should return an error when the password is incorrect", async () => {
    // Mocking userRepo.findByPhoneNumber to simulate an existing user
    const mockUser = {
      _id: "mockUserId",
      phoneNumber: "1234567890",
      password: "hashedPassword",
    };
    userRepo.findByPhoneNumber.mockResolvedValue(mockUser);

    // Mocking bcrypt.compare to simulate an incorrect password check
    mockCompare.mockResolvedValue(false);

    await login(mockRequest, mockResponse, mockNext);

    // Assert that the response status is 400 and an error is sent to next middleware
    expect(mockResponse.status).toHaveBeenCalledWith(400);
    expect(mockNext).toHaveBeenCalledWith(expect.any(Error));
    expect(mockResponse.json).not.toHaveBeenCalled();
  });

  it("should return an error when any field is missing", async () => {
    // Remove one required field from the request
    delete mockRequest.body.phoneNumber;

    await login(mockRequest, mockResponse, mockNext);

    // Assert that the response status is 400 and an error is sent to next middleware
    expect(mockResponse.status).toHaveBeenCalledWith(400);
    expect(mockNext).toHaveBeenCalledWith(expect.any(Error));
    expect(mockResponse.json).not.toHaveBeenCalled();
  });

  it("should return an error when the user is not found", async () => {
    // Mocking userRepo.findByPhoneNumber to simulate a user not found scenario
    userRepo.findByPhoneNumber.mockResolvedValue(null);

    await login(mockRequest, mockResponse, mockNext);

    // Assert that the response status is 400 and an error is sent to next middleware
    expect(mockResponse.status).toHaveBeenCalledWith(400);
    expect(mockNext).toHaveBeenCalledWith(expect.any(Error));
    expect(mockResponse.json).not.toHaveBeenCalled();
  });
});
