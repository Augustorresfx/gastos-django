const path = require('path')
const fs = require('fs').promises

class Model {
    constructor(pathName) {
        this.path = path.join(__dirname, pathName)
    }


async getProductById(id) {
    const data = await this.readData()
    const product = data.find(product => product,e.id == id)
    if (!product) {
        throw new Error ('Producto no encontrado')
    }
    return product
}

async add(product) {
    const data = await this.readData()
    const id = data[data.length - 1] ? data[data.length - 1].id : 0
    product.id = id + 1
    data.push(product)
    await this.writeData(data)
}

async getAll() {
    return this.readData()
}

writeData(data) {
    return fs.writeFile(this.path, JSON.stringify(data, null, 2))
}

async readData () {
    const raw = await fs.readFile(this.path, 'utf8')
    return JSON.parse(raw)
}
}

module.exports = Model