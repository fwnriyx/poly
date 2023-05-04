const jwt = require("jsonwebtoken");
const JWT_SECRET = require("../config.js");

var check = (req, res, next) => {
    const authHeader = req.headers.authorization;
    if (authHeader === null || authHeader === undefined || !authHeader.startsWith("Bearer ")) {
        res.status(401).send();
        return;
    }
    const token = authHeader.replace("Bearer ", "");
    jwt.verify(token, JWT_SECRET, { algorithms: ["HS256"] }, (error, decodedToken) => {
        if (error) {
            res.status(401).send();
            return;
        } else {
            req.decodedToken = decodedToken;
            next();
        }
    });
};
module.exports = check;
