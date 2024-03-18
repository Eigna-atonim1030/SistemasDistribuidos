const SHA256 = require('crypto-js/sha256');

class Bloque {
    constructor(indice, datos, hashAnterior = '') {
        this.indice = indice;
        this.timestamp = new Date();
        this.datos = datos;
        this.hashAnterior = hashAnterior;
        this.hash = this.calcularHash();
    }

    calcularHash() {
        return SHA256(this.indice + this.timestamp + JSON.stringify(this.datos) + this.hashAnterior).toString();
    }
}

class CadenaDeBloques {
    constructor() {
        this.cadena = [this.crearBloqueGenesis()];
    }

    crearBloqueGenesis() {
        return new Bloque(0, 'Bloque Génesis', '0');
    }

    obtenerUltimoBloque() {
        return this.cadena[this.cadena.length - 1];
    }

    agregarBloque(datos) {
        const nuevoBloque = new Bloque(this.obtenerUltimoBloque().indice + 1, datos, this.obtenerUltimoBloque().hash);
        this.cadena.push(nuevoBloque);
    }
}

module.exports = CadenaDeBloques;
