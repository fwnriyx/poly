const app = require("./controller/app");

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`BackEnd Server started on port ${PORT}`);
});
