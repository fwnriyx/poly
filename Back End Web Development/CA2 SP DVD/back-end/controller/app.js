//P2222811: Muhammad Fitri Amir bin Abdullah DAAA/FT/1B/06

var express = require('express');
var app = express();

var actors = require('../model/actors.js');
var login = require('../model/logIn.js');
var dvd = require('../model/dvd.js')
var staff = require('../model/staff.js')

const verifyToken = require('../auth/verifyToken.js')

//For multer storage engine
// const storage = multer.diskStorage({
//     destination: './images/product',
//     filename: (req, file, callback) => {
//         return callback(null, `${file.fieldname}_${Date.now()}${path.extname(file.originalname)}`) //make every image path unique 
//     }
// })
// const upload = multer({
//         storage: storage,
//         limits: { fileSize: 1000000 }, //limit file size 1MB
//     }).single('productimg') //only single file accepted


app.use(express.json());
app.use(express.urlencoded({ extended: false }))

var cors = require('cors');
app.options('*', cors());
app.use(cors());

// Endpoint 0 POST /login
app.post('/login', function (req, res) {
    console.log(req.body)
    var email = req.body.email;
    var password = req.body.password;

    login.loginUser(email, password, function (err, token, result) {
        if (err) {
            console.log(email, password)
            console.log("Error: Invalid user")
            res.status(404).json("Invalid email or password");
        } else if (!err) { //user successfully logged in
            console.log(token)
            res.status(200).json({staff_id: result[0].staff_id, token: token})
            console.log(result)
        } else {
            console.log(err)
            res.status(500).send("Unexpected Error!");
        }
    })
});

app.get('/category', function(req,res){
    dvd.category(function (err, result) {
        if (err) {
            console.log(err)
            res.status(404).json("Internal error");
        } else if (!err) {
            res.status(200).json({result})
            console.log(result)
        } else {
            console.log(err)
            res.status(500).send("Unexpected Error!");
        }
    })
});

app.post('/search/films', function(req, res) {
    console.log("Searching for films...");
    var films = {
        title: req.body.title,
        category: req.body.category,
        rental_rate: req.body.rental_rate
    }
    dvd.search(films, function(err, result) {
        if (err) {
            console.log(err);
            res.status(500).send("Unexpected Error!");
        } else {
            console.log("Reached Endpoint (product.search)");
            if(result == null) { // check if the result array is empty
                console.log("No films found with the given criteria");
                res.status(404).send("No films found with the given criteria");
            } else {
                // console.log("Films found: ",result);
                res.status(200).json(result);
            }
        }
    })
})

// Endpoint 3 POST /actors Add a new actor to the database (note: actors can have the same first_name and last_name)
app.post('/add/actors', function (req, res) {
    var { first_name, last_name } = req.body;
    if (first_name == "" || last_name == "") {
        res.status(400).json({ error_msg: 'missing data' });
    } else {
        actors.addActors(first_name, last_name, function (err, result) {
            if (!err) {
                res.status(201).json({ actor_id: `${result}` }); // more common
            } else {
                res.status(500).json({ error_msg: 'Internal server error' });
            }
        });
    }
});

// Endpoint 8: POST /customers Add a new customer to the database (note: customer’s email address is unique)
app.post('/add/customers', function (req, res) {
    var { store_id, first_name1, last_name1, email, address } = req.body;
    var { address1, address2, district, city_id, postal_code, phone } = address;
    staff.addCustomer(address1, address2, district, city_id, postal_code, phone, store_id, first_name1, last_name1, email, function (err, result) {
        if (err) {
            if (err.code = "ER DUP EMAIL") {
                res.status(409).json({ error_msg: 'email already exist' });
            } else {
                res.status(500).json({ error_msg: 'internal server error' });
            }
        } else {
            if (result == 0) {
                res.status(400).json({ "error_msg": "missing data" });
            }
            else {
                res.status(201).json(result);
            }
        }
    });
});

app.get('/DVD/:film_id', function (req, res) {
    var film_id = req.params.film_id;
    console.log(film_id)
    if (isNaN(film_id)) {
        res.status(404).json({ message: `Invalid input. Please try again.` });
    } else {
        dvd.showFilm(film_id, function (err, result) {
            if (err) {
                res.status(500).json({ message: `Internal server error` });
            } else if (result == null) {
                res.status(204);
            } else {
                res.status(200).json(result);
            }
        });
    }
});




module.exports = app