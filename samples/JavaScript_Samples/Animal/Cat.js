require("Animal.js")
class Cats extends Animals {
    constructor(name, age, color) {
        super(name, age);
        this.color = color;
    }
    
    color() {
        return `I'm ${this.color}`;
    }
}

let clara = new Cats("Clara", 33, "Grey");