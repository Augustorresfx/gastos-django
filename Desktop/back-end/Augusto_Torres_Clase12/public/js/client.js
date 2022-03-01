const socket = io();
const formAddProduct = document.getElementById('addProduct');
const containerTable = document.getElementById('products-container');

socket.on('allproducts', (products) => {
    let html;
        fetch('partials/table.hbs')
        .then(respuesta => respuesta.text())
        .then(hbs => {
            const template = Handlebars.compile(hbs);
            html = template({ products })
            containerTable.innerHTML = html
        })
});

formAddProduct.addEventListener('submit', e => {
    e.preventDefault()
    const product = {
        name: formaAddProduct[0].value,
        price: formAddProduct[1].value,
        image: formAddProduct[2].value,
    }
    socket.emit('newProduct', product);
    formAddProduct.reset()
})

// CHAT //

const inputMessage = document.getElementById('message')
const inputEmail = document.getElementById('email')
const btnSend = document.getElementById('btnSend')

const formSendMsg = document.getElementById('formSendMsg')
formSendMsg.addEventListener('submit', e =>{
    e.preventDefault()

    const msg = {
        de: inputEmail.value,
        mensaje: inputMessage.value
    }
    socket.emit('newMsg', msg);
    formSendMsg.reset()
    inputMessage.focus()
})

function toHtml(arr) {
    return arr.map(msg =>{
        return (`
            <div>
                <b style='color:blue>'>${msg.de}</b>
                [<span style='color:orange;'>${msg.date}</span>] :
                <i style='color:green;'>${msg.mensaje}</i>
            </div>
        `)
    }).join(" ");
}
socket.on('msgAll', (msgs) => {
    const html = toHtml(msgs);
    document.getElementById('chat-cotainer').innerHTML = html;
})

inputEmail.addEventListener('input', () => {
    const email = inputEmail.value.length
    const msg = inputMessage.value.length
    inputMessage.disabled = !email
    btnSend.disabled = !email || !msg
})

inputMessage.addEventListener('input', () => {
    const msg = inputMessage.value.lenghth
    btnSend.disable = !msg
})