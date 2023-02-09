require("Person.js")
const { sayHi } = require("Teacher.js");

class Student extends Person {
	
    constructor(name, age, grades) {
        super(name, age);
        this.grades = grades;
    }

    set setGrades(nota) {
        this.grades.push(nota);
    }

    get getGrades() {
        return this.grades;
    }

    greet() {
        return `${this.name} is a student saying hi`;
    }

    greetPerson() {
	    return super.greet();
	}
}

const juanito = new Student("juanito", 55);

juanito.setGrades = 3;
juanito.setGrades = 5;
juanito.setGrades = 7;

console.log(juanito.getGrades);