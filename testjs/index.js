const express = require('express')
const {spawn} = require('child_process');
const app = express()
const port = 3000
app.get('/', (req, res) => {
var largeDataSet = [];
 const python = spawn('C:/Users/User/AppData/Local/Programs/Python/Python38/python.exe', ['c:/Users/User/Desktop/ST Internship/annotatortool/testjs/script1.py']);
 python.stdout.on('data', function (data) {
  console.log('Pipe data from python script ...');
  largeDataSet.push(data);
 });
 python.on('close', (code) => {
 console.log(`child process close all stdio with code ${code}`);
 // send data to browser
 res.send(largeDataSet.join(""))
 const pythoner = spawn('C:/Users/User/AppData/Local/Programs/Python/Python38/python.exe', ['c:/Users/User/Desktop/ST Internship/annotatortool/testjs/script2.py']);
 });
 
})

app.listen(port, () => console.log(`Example app listening on port ${port}!`))