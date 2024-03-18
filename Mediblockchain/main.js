const SHA256 = CryptoJS.SHA256;

class Bloque {
    constructor(indice, timestamp, datos, hashAnterior = '') {
        this.indice = indice;
        this.timestamp = timestamp;
        this.datos = datos;
        this.hashAnterior = hashAnterior;
        this.hash = this.calcularHash();
    }

    calcularHash() {
        return SHA256(this.indice + this.hashAnterior + this.timestamp + JSON.stringify(this.datos)).toString();
    }
}

class CadenaDeBloques {
    constructor() {
        this.cadena = [this.crearBloqueGenesis()];
    }

    crearBloqueGenesis() {
        return new Bloque(0, "01/01/2017", "Bloque Génesis", "0");
    }

    obtenerUltimoBloque() {
        return this.cadena[this.cadena.length - 1];
    }

    agregarBloque(nuevoBloque) {
        const bloqueAnterior = this.obtenerUltimoBloque();
        nuevoBloque.hashAnterior = bloqueAnterior.hash; // Utilizar el hash del bloque anterior como hashAnterior
        nuevoBloque.hash = nuevoBloque.calcularHash(); // Calcular el hash del bloque actual
        this.cadena.push(nuevoBloque);

        console.log("Hash Anterior: ", bloqueAnterior.hash);
        console.log("Nuevo Hash: ", nuevoBloque.hash);
    }

    obtenerTodosLosBloques() {
        return this.cadena.map(bloque => {
            return {
                indice: bloque.indice,
                timestamp: bloque.timestamp,
                datos: bloque.datos,
                hashAnterior: bloque.hashAnterior,
                hash: bloque.hash
            };
        });
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const formulario = document.querySelector('#formularioMedicamento');
    const listaBloques = document.getElementById('lista-bloques');

    const cadenaMedicamentos = new CadenaDeBloques();

    actualizarListaBloques(); // Mostrar bloques al cargar la página

    // Cambiar el evento de submit a click en el botón de enviar
    document.getElementById('enviarBtn').addEventListener('click', function(event) {
        event.preventDefault(); // Prevenir el envío predeterminado del formulario
    
        const nombreMedicamento = document.getElementById('nombreMedicamento').value;
        const lote = document.getElementById('lote').value;
        const fechaFabricacion = document.getElementById('fechaFabricacion').value;
        const fechaExpiracion = document.getElementById('fechaExpiracion').value;
        const fabricante = document.getElementById('fabricante').value;
//----------------------------------------------------------------------------------------------------------    
        // Obtener los valores del formulario y crear un objeto nuevoBloqueDatos
        const nuevoBloqueDatos = {
            nombreMedicamento,
            lote,
            fechaFabricacion,
            fechaExpiracion,
            fabricante
        };
        
        const nuevoBloque = new Bloque(
            Date.now(),                 // indice
            new Date(),                 // timestamp
            nuevoBloqueDatos,           // datos
            ''                          // hashAnterior
        );
        

        // Agregar el nuevo bloque a la cadena y actualizar la lista de bloques
        cadenaMedicamentos.agregarBloque(nuevoBloque);
        actualizarListaBloques();
    });
//----------------------------------------------------------------------------------------------------------
    function actualizarListaBloques() {
        listaBloques.innerHTML = ''; // Limpiar la lista antes de actualizar
    
        const bloques = cadenaMedicamentos.obtenerTodosLosBloques();
        // Comenzar desde el segundo bloque para omitir el bloque génesis
        for (let i = 1; i < bloques.length; i++) {
            const bloque = bloques[i];
            const elementoBloque = document.createElement('li');
            const datosBloque = document.createElement('div');
            datosBloque.classList.add('datos-bloque');
    
            // Mostrar cada propiedad del bloque
            const keys = Object.keys(bloque.datos);
            keys.forEach(key => {
                const propiedad = document.createElement('div');
                propiedad.textContent = `${key}: ${bloque.datos[key]}`;
                datosBloque.appendChild(propiedad);
            });
    
            // Mostrar el hash del bloque
            const hash = document.createElement('div');
            hash.textContent = `Hash: ${bloque.hash}`;
            datosBloque.appendChild(hash);
    
            // Agregar los datos del bloque al elemento de lista
            elementoBloque.appendChild(datosBloque);
            listaBloques.appendChild(elementoBloque);
        }
    }
});
