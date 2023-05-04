const app = require("./controller/app");

const PORT = 3000;
const HOSTNAME = "localhost";

app.listen(PORT, HOSTNAME, () => {
    console.log(`Back End Server started on port ${PORT}`);
});
