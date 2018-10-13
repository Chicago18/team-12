INSERT INTO user(username, password, firstname, lastname, type)
VALUES 
("sally123", "password", "Sally", "Watson", "s"),
("billy123", "password", "Billy", "Watson", "p"),
("william123", "password", "William", "Smith", "a")
;

INSERT INTO admin(username, firstname, lastname)
VALUES 
("william123", "William", "Smith")
;

INSERT INTO parent(username, firstname, lastname, familytype,
				   housingstatus, foodstamps, reducedlunch, insurance,
				   referral, clientid, incomesource1, incomesource2,
				   incomesource3, incomesource4, incomesource5, incomesource6,
				   incomesource7, incomesource8)
VALUES
("billy123", "Billy", "Watson", "Relative", "Rent",
 "y", "n", "n", "Bob", 300, "y", "y", "n", "n", "n", "n", "n", "y");

INSERT INTO student(username, firstname, lastname, middleinitial, parentid,
					gender, age, birthdate, phonenumber, ethnicity, race,
					currentgrade, school, disability, communityarea, registered)
VALUES
("sally123", "Sally", "Watson", "K", "billy123", 3, "female", "01/01/2000", "1234567890", "Hispanic", "Spanish",
 "3", "Schoolington Elementary School", "No", "Schoolington", "Y")