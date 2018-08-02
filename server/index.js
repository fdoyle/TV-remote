const express = require('express')
const app = express()

const cec = require('hdmi-cec')

const cecRemote = cec.Remote;
const commander = cec.Commander;
const television = cec.Television;
const monitor = cec.CecMonitor;
const receiver = cec.Receiver;

const remote = new cecRemote();

app.get('/', (req, res)=> res.send('Hello World'))
app.listen(3000, ()=>console.log('Listening on port 3000'))

app.post('/on', (req, res)=>{

})

app.post('/off',(req, res)=>{

})

// remote.on('keypress', evt=>{
//     console.log(`user pressed the key "${evt.key}" with code "${evt.keyCode}"`);
// })