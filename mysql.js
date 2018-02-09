var pwd = require("config");

var mysql      = require('mysql');
var connection = mysql.createConnection({
    host     : 'localhost',
    user     : 'shared',
    password : pwd,
    database : 'volvox'
});

connection.connect();

connection.query('SELECT * FROM dhtlogger', function (error, results, fields) {
    if (error) throw error;
    console.log('The data is: ', results);
});

connection.end();
