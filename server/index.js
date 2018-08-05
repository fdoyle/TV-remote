const express = require('express')
const app = express()

const bodyParser = require('body-parser')

var nodecec = require('node-cec')

var NodeCec = nodecec.NodeCec
var CEC     = nodecec.CEC;
var cec = new NodeCec('node-cec-monitor')


app.use(bodyParser.json())

cec.once('ready', function (client) {
    console.log(' -- READY -- ');
    client.sendCommand(0xf0, CEC.Opcode.GIVE_DEVICE_POWER_STATUS);
    startServer();
});

process.on('SIGINT', function () {
    if (cec != null) {
        cec.stop();
    }
    process.exit();
});


cec.on('ROUTING_CHANGE', function (packet, fromSource, toSource) {
    console.log('Routing changed from ' + fromSource + ' to ' + toSource + '.');
});

cec.on('', function (packet, fromSource, toSource) {
    console.log('Routing changed from ' + fromSource + ' to ' + toSource + '.');
});



function startServer() {
    app.get('/', (req, res) => res.send("This is the remote api"))

    app.post('/on', (req, res) => {

    })

    app.post('/off', (req, res) => {

    })

    app.post('/input', (req, res) => {

    })

    app.post('/raw', (req, res)=>{
        var transaction = req.body.transaction
        console.log(JSON.stringify(transaction))
        cec.send(transaction);
        // var intTransaction = parseInt(transaction, 16)
        // cec.sendCommand(intTransaction)
    })
    app.listen(3000, () => console.log('Listening on port 3000'))
}
cec.start('cec-client', '-d', '8', '-b', 'r')