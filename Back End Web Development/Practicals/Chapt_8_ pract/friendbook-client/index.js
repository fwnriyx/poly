const express = require("express");
const app = express();

app.get("/", (req, res) => { // get homepage (index.html)
  res.sendFile("/public/index.html", { root: __dirname });
});

app.get("/users/:id", (req, res) => {
  res.sendFile("/public/user.html", { root: __dirname });
});

app.get("/users/", (req, res) => {
  res.sendFile("/public/users.html", { root: __dirname });
});

app.get("/login/", (req, res) => {
    res.sendFile("/public/login.html", { root: __dirname });
});
  

const PORT = 3001;
app.listen(PORT, () => {
//   console.log(`Client server has started listening on port ${PORT}`);
    console.log(`FrontEnd server has started listening on port ${PORT}`);
});
