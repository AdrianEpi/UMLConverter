
class Person {
    
    constructor(name, books) {
        this.name = name;
        this.books = books || [];
    }

    // setter
    set setBook(book) {
        this.books.push(book);
    }

    // getter
    get getBooks() {
        return this.books;
    }

    // method
    lookBookByTitle(title) {
        return this.books.find((item) => item.title === title);
    }

    static tryGreet(name) {
        return `${name} is saying hi`;
    }

    greet() {
        return `${this.name} is saying hi `;
    }
}

const person1 = new Person("Ignacio");
person1.setBook = { title: "Papelucho", author: "Marcela Paz" };
person1.setBook = {
    title: "El principito",
    author: "Antoine de Saint-Exupéry",
};

console.log(person1.lookBookByTitle("Papelucho"));

console.log(person1.getBooks);