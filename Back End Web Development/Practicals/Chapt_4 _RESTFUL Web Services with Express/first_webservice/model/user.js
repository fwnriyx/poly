module.exports = {
    maxUserId: 2,
    userData: [
        {
            "userid": 1,
            "username": "John",
            "email": "john@gmail.com",
            "role": "user",
            "password": "abc123"
        },
        {
            "userid": 2,
            "username": "mary",
            "email": "mary@gmail.com",
            "role": "user",
            "password": "abc123"
        }
    ],
    createUser: function (newUserDetail, callback)  {

    },
    
    retrieveAllUser: function (callback){
        return callback(null, this.userData);
    },

    retrieveUser : function (userid, callback) {
        const located = this.userData.findIndex((element) => element.userid == userid);
        return callback (null, this.userData[located]);
    },

    updateUser : function (userid, callback) {

    },

    deleteUser : function (userid, callback) {

    }
}
