INSERT INTO Type (type_id, type_name)
VALUES
(1, 'Grass'),
(2, 'Fire'),
(3, 'Water'),
(4, 'Normal'),
(5, 'Flying');

INSERT INTO Pokemon (pokemon_id, pokemon_name, primary_type_id, secondary_type_id)
VALUES
(1, 'Bulbasaur', 1, NULL),
(2, 'Charmander', 2, NULL),
(3, 'Squirtle', 3, NULL),
(4, 'Eevee', 4, NULL),
(5, 'Pidgey', 4, 5);

INSERT INTO Move (move_id, move_name, power, type_id)
VALUES
(1, 'Tackle', 35, 4),
(2, 'Water Gun', 40, 3),
(3, 'Ember', 40, 2),
(4, 'Vine Whip', 40, 1),
(5, 'Wing Attack', 65, 5),
(6, 'Headbutt', 70, 4),
(7, 'Return', 100, 4);

INSERT INTO Pokemon_Move (pokemon_id, move_id)
VALUES
(1, 1), (1, 4), (1, 7), -- Bulbasaur
(2, 1), (2, 3), (2, 7), -- Charmander
(3, 1), (3, 2), (3, 7), -- Squirtle
(4, 1), (4, 6), (4, 7), -- Eevee
(5, 1), (5, 5), (5, 7); -- Pidgey

