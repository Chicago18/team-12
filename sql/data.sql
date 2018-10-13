INSERT INTO user(username, password, type)
VALUES 
("sally123", "password", "s"),
("billy123", "password", "p"),
("william123", "password", "a")
;

INSERT INTO admin(username, firstname, lastname)
VALUES 
("william123", "William", "Smith")
;

INSERT INTO parent(username, firstname, lastname, familytype,
				   housingstatus, foodstamps, reducedlunch, insurance,
				   referral, clientid, incomesource1, incomesource2
				   incomesource3, incomesource4, incomesource5, incomesource6,
				   incomesource7, incomesource8)
VALUES
("billy123", "Billy", "Watson", "Relative", "Rent",
 "")