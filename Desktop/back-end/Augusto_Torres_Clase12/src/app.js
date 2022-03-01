const http = require('http')
const path = require('path')
const express= require('express')
const app = express()
const server = http.createServer(app)
const { Server } = require('socket.io');
const Model = require ('./models/model')
const modelProducts = new Model('../data/productos.json')
const modelChat = new Model('../data/msgChat.json')
const io = new Server(server);

const PORT = process.env.PORT || 8080;


app.use(express.json())
app.use(express.urlencoded({ extended: true }))
app.use(express.static('public'))


app.get('/', (req, res) => res.sendFile(path.join(__dirname, 'public/index.html')))


io.on('connection', async (socket) => {
    const products = await modelProducts.getAll()

    socket.emit('allproducts',products)

    socket.on('newProduct', async (product) => {
        const newProduct = await modelProducts.add(product)
        socket.emit('products', newProduct)
    })

    socket.emit('msgAll', await modelChat.getAll());

    socket.on('newMsg', async msg => {
        msg.date = new Date().toLocaleString()
        await modelChat.add(msg)
        socket.emit('msgs', await modelChat.getAll());
    })

})

server.listen(PORT, () => console.log (`Escuchando en el puerto: ${PORT}`));