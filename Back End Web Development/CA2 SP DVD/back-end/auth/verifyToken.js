var jwt = require('jsonwebtoken');
var config = require('../config');

function verifyToken(req, res, next){
    var token = req.headers['authorization']; //retrieve authorization header’s content
    console.log(token);

    if (!token || !token.includes('Bearer')) { //process the token
        res.status(403);
        return res.send({auth:'false', message:'Not authorized!'});
    }

    else {
        token = token.split('Bearer ')[1]; //obtain the token’s value
        console.log(token);
        jwt.verify(token, config.key, function(err, decodedToken) { //verify token
            if (err) {
                console.log("From verifyToken.js: Error occured when verifying token");
                res.status(403);
                return res.send({auth:false, message:'Not authorized!'});
            }
            else {
                req.decodedUserid = decodedToken.userid; //decode the userid and store in req for use
                req.decodedType = decodedToken.type; //decode the user type and store in req for use
                next();
            }
        });
    }
}

module.exports = verifyToken;
