class Animals {
    constructor(nombre, especie) {
        this.nombre = nombre;
        this.especie = especie;
    }
    
    sing() {
        return `${this.nombre} can singr`;
    }
    
    dance() {
        return `${this.nombre} can dance`; // This is a comment
    }
}
/* 
 * this is another comment
*/

let bongo = new Animals("Bongo", "Peludo");
console.log(bongo);