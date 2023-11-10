import symptomRepo from "../db/repos/symptomRepo.js"

export const findAll = async (req, res, next) => {
    const symptoms = await symptomRepo.retrieveAll();
    res.status(200).json({
      messagse: symptoms,
    });
  };
