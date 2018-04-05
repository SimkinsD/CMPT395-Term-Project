insert into 395db.user_myuser
(password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
values ('pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 1, 'admin', 'John', 'Doe', 'email@email.com', 1, 1, '2018-03-25 19:50:40.005625'),
('pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'smith1', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
('pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'jones1', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
('pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'trump1', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
('pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'doe1', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
('pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'smith2', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
('pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'sedin1', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
('pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'naslund1', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
('pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'linden1', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625'),
('pbkdf2_sha256$100000$fkQ5BjtLLXBu$YuIg3NypmH5KUISO30IHMHDM6dRVU4qNHL0n72hEBhs=', 0, 'crosby1', 'first', 'last', 'email@email.com', 0, 1, '2018-03-25 19:50:40.005625');

insert into 395db.user_family (familyID, family_name, email, user_id)
values ('Teacher', 'email@email.com', 1),
('Smith', 'email@email.com', 2),
('Jones', 'email@email.com', 3),
('Trump', 'email@email.com', 4),
('Doe', 'email@email.com', 5),
('Smith', 'email@email.com', 6),
('Sedin', 'email@email.com', 7),
('Naslund', 'email@email.com', 8),
('Linden', 'email@email.com', 9),
('Crosby', 'email@email.com', 10);

insert into 395db.user_volunteer (first_name, last_name, email, family_id)
values ('Tom', 'Smith', 'email@email.com', 2),
('Jack', 'Jones', 'email@email.com', 3),
('Donald', 'Smith', 'email@email.com', 4),
('John', 'Doe', 'email@email.com', 5),
('Dianna', 'Black', 'email@email.com', 5),
('Tina', 'Smith', 'email@email.com', 6),
('Daniel', 'Sedin', 'email@email.com', 7),
('Markus', 'Naslund', 'email@email.com', 8),
('Henrik', 'Sedin', 'email@email.com', 7);


insert into 395db.user_child (first_name, last_name, classroom, family_id)
values ('Timmy', 'Smith', 'red', 2),
('Jane', 'Smith', 'blue', 2),
('Tommy', 'Jones', 'red', 3),
('Jr.', 'Trump', 'green', 4),
('Jane', 'Doe', 'blue', 5),
('Charlie', 'Smith', 'red', 6),
('Sally', 'Sedin', 'blue', 7),
('Chuck', 'Naslund', 'green', 8),
('Jim', 'Naslund', 'green', 8),
('Stacy', 'Park', 'blue', 8),
('Sally', 'Bond', 'red', 8);



insert into 395db.user_signup (date, start_time, end_time, classroom, volunteer_id)
values ('2018-04-04', '8:45:00', '11:00:00', 'red', 3),
('2018-04-04', '8:45:00', '10:00:00', 'green', 4),
('2018-04-04', '8:45:00', '12:00:00', 'blue', 5),
('2018-04-04', '12:50:00', '15:00:00', 'red', 6),
('2018-04-04', '13:00:00', '15:45:00', 'blue', 7),
('2018-04-04', '12:00:00', '13:00:00', 'red', 8),
('2018-04-04', '12:00:00', '13:00:00', 'blue', 9),
('2018-04-04', '12:00:00', '13:00:00', 'green', 1),
('2018-04-04', '13:30:00', '15:30:00', 'green', 2),
('2018-04-05', '8:45:00', '11:00:00', 'red', 3),
('2018-04-05', '8:45:00', '10:00:00', 'green', 4),
('2018-04-05', '8:45:00', '12:00:00', 'blue', 5),
('2018-04-05', '12:50:00', '15:00:00', 'red', 6),
('2018-04-05', '13:00:00', '15:45:00', 'blue', 7),
('2018-04-05', '12:00:00', '13:00:00', 'red', 8),
('2018-04-05', '12:00:00', '13:00:00', 'blue', 9),
('2018-04-05', '12:00:00', '13:00:00', 'green', 1),
('2018-04-05', '13:30:00', '15:30:00', 'green', 2),
('2018-04-06', '8:45:00', '11:00:00', 'red', 3),
('2018-04-06', '8:45:00', '10:00:00', 'green', 4),
('2018-04-06', '8:45:00', '12:00:00', 'blue', 5),
('2018-04-06', '12:50:00', '15:00:00', 'red', 6),
('2018-04-06', '13:00:00', '15:45:00', 'blue', 7),
('2018-04-06', '12:00:00', '13:00:00', 'red', 8),
('2018-04-06', '12:00:00', '13:00:00', 'blue', 9),
('2018-04-06', '12:00:00', '13:00:00', 'green', 1),
('2018-04-06', '13:30:00', '15:30:00', 'green', 2),
('2018-04-09', '8:45:00', '11:00:00', 'red', 3),
('2018-04-09', '8:45:00', '10:00:00', 'green', 4),
('2018-04-09', '8:45:00', '12:00:00', 'blue', 5),
('2018-04-09', '12:50:00', '15:00:00', 'red', 6),
('2018-04-09', '13:00:00', '15:45:00', 'blue', 7),
('2018-04-09', '12:00:00', '13:00:00', 'red', 8),
('2018-04-09', '12:00:00', '13:00:00', 'blue', 9),
('2018-04-09', '12:00:00', '13:00:00', 'green', 1),
('2018-04-09', '13:30:00', '15:30:00', 'green', 2),
('2018-04-10', '8:45:00', '11:00:00', 'red', 3),
('2018-04-10', '8:45:00', '10:00:00', 'green', 4),
('2018-04-10', '8:45:00', '12:00:00', 'blue', 5),
('2018-04-10', '12:50:00', '15:00:00', 'red', 6),
('2018-04-10', '13:00:00', '15:45:00', 'blue', 7),
('2018-04-10', '12:00:00', '13:00:00', 'red', 8),
('2018-04-10', '12:00:00', '13:00:00', 'blue', 9),
('2018-04-10', '12:00:00', '13:00:00', 'green', 1),
('2018-04-10', '13:30:00', '15:30:00', 'green', 2),
('2018-04-11', '8:45:00', '11:00:00', 'red', 3),
('2018-04-11', '8:45:00', '10:00:00', 'green', 4),
('2018-04-11', '8:45:00', '12:00:00', 'blue', 5),
('2018-04-11', '12:50:00', '15:00:00', 'red', 6),
('2018-04-11', '13:00:00', '15:45:00', 'blue', 7),
('2018-04-11', '12:00:00', '13:00:00', 'red', 8),
('2018-04-11', '12:00:00', '13:00:00', 'blue', 9),
('2018-04-11', '12:00:00', '13:00:00', 'green', 1),
('2018-04-11', '13:30:00', '15:30:00', 'green', 2);



insert into 395db.fieldtrip_fieldtrip (title, location, info, date)
values('Waterpark', 'WEM', 'Please bring swimsuits', '2018-04-10'),
('Park visit', 'forest place', 'Bring bug spray and food', '2018-04-11'),
('Hospital tour', 'Glenn Rose', 'Don\'t come if sick', '2018-04-12');
