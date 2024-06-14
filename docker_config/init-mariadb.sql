GRANT ALL PRIVILEGES ON *.* TO 'maxscale_user'@'%';
FLUSH PRIVILEGES;

CREATE DATABASE books;
USE books;

CREATE TABLE books (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(255) NOT NULL
);

INSERT INTO books (name, author, genre) VALUES ('1984', 'George Orwell', 'Dystopian political fiction');

INSERT INTO books (name, author, genre) VALUES ('The Da Vinci Code', 'Dan Brown', 'Mystery, Thriller');
INSERT INTO books (name, author, genre) VALUES ('The Brothers Karamazov', ' Fyodor Dostoevsky', 'Philosophical novel');
