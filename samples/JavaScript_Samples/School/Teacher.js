require("Person.js")
require("Student.js")
class Teacher extends Person {
    //#teacher = "Teacher";

    constructor() {
    	this.teacher = "Teacher"
    }

    addNewTeacher() {
        const clone = templateTeacher.cloneNode(true);
        clone.querySelector("h5").textContent = this.name;
        clone.querySelector("h6").textContent = this.teacher;
        clone.querySelector(".lead").textContent = this.age;
        return clone;
    }
}

function sayHi(person) {
    function give2(num) {
        num = 2
        return num
    }
    return person.greet()
}

module.exports = { sayHi }