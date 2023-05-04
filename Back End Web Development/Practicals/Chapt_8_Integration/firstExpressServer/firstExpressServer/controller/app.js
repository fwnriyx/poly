var express = require('express');
var bodyParser = require('body-parser');
var app = express();
var user = require('../model/user.js');
var verifyToken = require('../auth/verifyToken.js');

// These 3 lines are important
// Do "npm i cors" first
// Add these 3 lines somewhere near top
var cors = require('cors');
app.options('*',cors());
app.use(cors());

var urlencodedParser=bodyParser.urlencoded({extended:false});


app.use(bodyParser.json());
app.use(urlencodedParser);

app.use('/image', express.static('public/image/'))

app.get('/user/:userid',function(req, res){
    var id = req.params.userid;

    user.getUser(id, function(err, result){
        if(!err){
            res.send(result);
        }else{
            res.status(500).send("Some error");
        }
    });
}); 

app.post('/user/login',function(req, res){
    var email=req.body.email;
    var password = req.body.password;

    user.loginUser(email, password, function(err, token, result){
        if(!err){
			res.statusCode = 200;
			  res.setHeader('Content-Type', 'application/json');
			  delete result[0]['password'];//clear the password in json data, do not send back to client
			  console.log(result);
			res.json({success: true, UserData: JSON.stringify(result), token:token, status: 'You are successfully logged in!'}); 
			res.send();
		}else{
            res.status(500);
            res.send(err.statusCode);
        }
    }); 
}); 


app.post('/user/logout', function(req,res){
	console.log("..logging out.");
	//res.clearCookie('session-id'); //clears the cookie in the response
	//res.setHeader('Content-Type', 'application/json');
  	res.json({success: true, status: 'Log out successful!'});

});



app.put('/user',verifyToken,function(req,res){
	var username = req.body.username;
	var email = req.body.email;
	var role = req.body.role;
	
	// user.updateUser(username,email,role,function(err,result){
	user.updateUser(username,email,role,req.userid,function(err,result){
		if(!err){
			console.log("Update successful");
			res.statusCode = 200;
  			res.setHeader('Content-Type', 'application/json');
  			res.json({success: true, result: result, status: 'Record updated successfully!'});
		}else{
			res.status(500);
			res.send(err.statuscode);
		}
	})
}); 


app.post('/user',function(req,res){
	
	var username = req.body.username;
	var email = req.body.email;
	var role = req.body.role;
	var password = req.body.password;
	var pic = req.body.pic;
	
	user.addUser(username,email,role,password,pic,function(err,result){
	if(!err){
		res.status(200);
		res.send(result);
	}else{
		res.status(500);
		res.send("{\"message\":\"Some error!\"}");
	}
	});
});

app.get('/user',function(req, res){

    user.getUsers(function(err, result){
        if(!err){
            res.send(result);
        }else{
            res.status(500).send(null);
        }
    });
}); 

module.exports = app;