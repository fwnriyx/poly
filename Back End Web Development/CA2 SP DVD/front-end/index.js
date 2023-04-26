const express = require("express");
const app = express();

app.use(express.static('public'));

app.get("/", (req, res) => { // get homepage (index.html)
  res.sendFile("/public/index.html", { root: __dirname });
});

app.get("/category.html", (req, res) => { // get homepage (index.html)
  res.sendFile("/public/index.html", { root: __dirname });
});

app.get("/users/:id", (req, res) => {
  res.sendFile("/public/user.html", { root: __dirname });
});

app.get("/dvd/", (req, res) => {
  res.sendFile("/public/dvd.html", { root: __dirname });
});

app.get("/login/", (req, res) => {
    res.sendFile("/public/login.html", { root: __dirname });
});
  
app.post("/login", (req, res) => {
  res.sendFile("/public/login.html", { root: __dirname });
});

app.get("/admin", (req, res) => {
  res.sendFile("/public/add.html", { root: __dirname });
});

app.post("/admin", (req, res) => {
  res.sendFile("/public/add.html", { root: __dirname });
});

const PORT = 3001;
app.listen(PORT, () => {
    console.log(`FrontEnd server has started listening on port ${PORT}`);
});
