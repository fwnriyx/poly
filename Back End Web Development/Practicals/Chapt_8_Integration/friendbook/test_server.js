const user = require("./model/user");

// user.findByID(3, (error, user) => {
//     if (error) {
//         console.log(error);
//         return;
//     };
//     console.log(user);
// });

// user.findByID(1000, (error, user) => {  // record does not exist
//     if (error) {
//         console.log(error);
//         return;
//     };
//     console.log(user);
// });

// user.findAll((error, users) => {
//     if (error) {
//       console.log(error);
//       return;
//     }
//     console.log(users);
// });

// const editedUser = {
//     full_name: "chad thunder",
//     username: "chad",
//     bio: "This is the super cool Chad Thunder!!",
//     date_of_birth: "1980-10-10"
// };

// // provide the user id of the user with full_name "Julius"
// // it may not be 5 for you
// user.edit(4, editedUser, (error) => {
//     if (error) {
//         console.log(error);
//         return;
//     };
// });

const editedUser = {
    bio: "I am RON!"
};

// provide the user id of the user with full_name "Julius"
// it may not be 5 for you
user.edit(3, editedUser, (error) => {
    if (error) {
        console.log(error);
        return;
    };
});

  