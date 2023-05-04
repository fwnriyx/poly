const user = require("./model/user");

// user.findByID(1000, (error, user) => {
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
  
const editedUser = {
  // full_name: "Julius Lim",
  username: "julius",
  bio: "This is Chad!"//,
  // date_of_birth: "2001-10-16"
};

// provide the user id of the user with full_name "Julius"
// it may not be 5 for you
user.edit(4, editedUser, (error) => {
    if (error) {
      console.log(error);
      return;
    };
});
