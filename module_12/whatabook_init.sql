CREATE DATABASE whatabook;

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

use whatabook;

CREATE TABLE user 
(
    user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(75) NOT NULL,
    last_name VARCHAR(75) NOT NULL
);

CREATE TABLE book 
(
    book_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    book_name VARCHAR(200) NOT NULL,
    details VARCHAR(500) NOT NULL,
    author VARCHAR(200) NOT NULL
);

CREATE TABLE store 
(
    store_id int NOT NULL PRIMARY KEY,
    locale VARCHAR(500) NOT NULL
);


CREATE TABLE wishlist 
(
    wishlist_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    book_id INT NOT NULL,
    CONSTRAINT fkey_user,
    FOREIGN KEY (user_id)
        REFERENCES user(user_id),
    CONSTRAINT fkey_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
);

INSERT INTO store (store_id, locale) VALUES (1,'1000 Gavin Rd S, Bellevue, NE 68005');

INSERT INTO user (user_id, first_name, last_name) VALUES (1, 'Darth', 'Vader');
INSERT INTO user (user_id, first_name, last_name) VALUES (2, 'Luke', 'Skywalker');
INSERT INTO user (user_id, first_name, last_name) VALUES (3, 'Han', 'Solo');

INSERT INTO book (book_id, book_name, details, author) VALUES (1, 'Star Wars', 'The Novelization of the movie: STAR WARS', 'Alan Dean Foster');
INSERT INTO book (book_id, book_name, details, author) VALUES (2, 'The Empire Strikes Back', 'The Novelization of the movie: The Empire Strikes Back', 'Donald F. Glut');
INSERT INTO book (book_id, book_name, details, author) VALUES (3, 'The Return of the Jedi', 'The Novelization of the movie: The Return of the Jedi', 'James Khan');
INSERT INTO book (book_id, book_name, details, author) VALUES (4, 'The Phantom Menace', 'The Novelization of the movie: The Phantom Menace', 'Terry Brooks');
INSERT INTO book (book_id, book_name, details, author) VALUES (5, 'Attack of the Clones', 'The Novelization of the movie: Attack of the Clones', 'R. A. Salvatore');
INSERT INTO book (book_id, book_name, details, author) VALUES (6, 'Revenge of the Sith', 'The Novelization of the movie: Revenge of the Sith', 'Matthew Stover');
INSERT INTO book (book_id, book_name, details, author) VALUES (7, 'The Force Awakens', 'The Novelization of the movie: The Force Awakens', 'Alan Dean Foster');
INSERT INTO book (book_id, book_name, details, author) VALUES (8, 'The Last Jedi', 'The Novelization of the movie: The Last Jedi', 'Jason Fry');
INSERT INTO book (book_id, book_name, details, author) VALUES (9, 'The Rise of Skywalker', 'The Novelization of the movie: The Rise of Skywalker', 'Rae Carson');

INSERT INTO wishlist (wishlist_id, user_id, book_id) VALUES (1, 1, 3);
INSERT INTO wishlist (wishlist_id, user_id, book_id) VALUES (2, 2, 8);
INSERT INTO wishlist (wishlist_id, user_id, book_id) VALUES (3, 3, 7);