const form = document.getElementById('addProduct');

const socket = io();
const formAddProduct = document.getElementById('addProduct')
formAddGame.addEventListener('submit', e => {
    e.preventDefault()
    const product = {
        name: formAddProduct[0].value,
        price: formAddProduct[1].value,
        image: formAddProduct[2].value
    }
    socket.emit('newProduct', product);
    formAddProduct.reset()
})

socket.on('allproducts', (products) => {
let containerTable = document.getElementById('products-container');

let html;
    fetch('partials/table.hbs')
    .then(respuesta => respuesta.text())
    .then(hbs => {
            const template = HandleBars.compile(hbs);
            html= template({products})
            containerTable.innerHTML = html
        })

});