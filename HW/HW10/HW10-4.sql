CREATE TABLE "cards"(
    "user_id" INTEGER NOT NULL,
    "card_id" INTEGER NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "charge" INTEGER NOT NULL,
    "expiration_date" DATE NULL
);
ALTER TABLE
    "cards" ADD PRIMARY KEY("card_id");
COMMENT
ON COLUMN
    "cards"."name" IS 'Only can be: single card - credit card - term card';
CREATE TABLE "bankaccount"(
    "user_id" INTEGER NOT NULL,
    "Account_id" INTEGER NOT NULL,
    "owner_name" VARCHAR(255) NOT NULL,
    "national_code" VARCHAR(255) NOT NULL,
    "balance" INTEGER NOT NULL
);
ALTER TABLE
    "bankaccount" ADD PRIMARY KEY("Account_id");
ALTER TABLE
    "bankaccount" ADD CONSTRAINT "bankaccount_national code_unique" UNIQUE("national_code");
CREATE TABLE "users"(
    "user_id" INTEGER NOT NULL,
    "full_name" VARCHAR(255) NOT NULL,
    "age" INTEGER NOT NULL
);
ALTER TABLE
    "users" ADD PRIMARY KEY("user id");
CREATE TABLE "trips"(
    "user_id" INTEGER NOT NULL,
    "trip_id" INTEGER NOT NULL,
    "card_id" INTEGER NOT NULL,
    "origin" VARCHAR(255) NOT NULL,
    "destination" VARCHAR(255) NOT NULL,
    "cost" INTEGER NOT NULL
);
ALTER TABLE
    "trips" ADD PRIMARY KEY("trip_id");
ALTER TABLE
    "cards" ADD CONSTRAINT "cards_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "users"("user_id");
ALTER TABLE
    "trips" ADD CONSTRAINT "trips_card_id_foreign" FOREIGN KEY("card_id") REFERENCES "cards"("card_id");
ALTER TABLE
    "bankaccount" ADD CONSTRAINT "bankaccount_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "users"("user_id");
ALTER TABLE
    "trips" ADD CONSTRAINT "trips_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "users"("user_id");





-- ======================================================================
-- input data


-- SELECT * FROM bankaccount;
-- SELECT * FROM trips;

-- INSERT INTO users(user_id, full_name, age)
-- VALUES (1001, 'Reza Amin', 22),
--        (1002, 'Parsa Ahmaripour', 22), 
--        (1003, 'Mti Farokh', 19);

-- INSERT INTO bankaccount(user_id, account_id, owner_name, national_code, balance)
-- VALUES (1001, 2001, 'reza amin', '123445', 50000),
--        (1002, 2002, 'parsa ahmaripour', '123446', 20000),
--        (1003, 2003, 'Mti Farokh', '123447', 30000);


-- INSERT INTO cards(user_id, card_id, card_name, charge, expiration_date)
-- VALUES (1001, 3001, 'single', 10, NULL),
--        (1001, 3002, 'credit', 100, NULL),
--        (1001, 3003, 'term', 80, '2022-8-30'),
--        (1002, 3004, 'single', 10, NULL),
--        (1002, 3005, 'credit', 120, NULL),
--        (1002, 3006, 'term', 90, '2022-9-20'),
--        (1003, 3007, 'single', 10, NULL),
--        (1003, 3008, 'credit', 220, NULL),
--        (1003, 3009, 'term', 100, '2022-9-20');




-- 1
-- SELECT DISTINCT trips.user_id, users.full_name
-- FROM trips
-- JOIN users
-- ON users.user_id=trips.user_id;

-- 2
-- SELECT DISTINCT trips.user_id, trip_id, users.full_name, cards.card_name
-- FROM trips
-- JOIN users
-- ON users.user_id=trips.user_id
-- JOIN cards ON cards.card_id=trips.card_id
-- WHERE cards.card_name='single';


-- SELECT * FROM trips;

-- 3
-- SELECT COUNT(cards.card_name) AS number_of_card_used, trips.user_id, users.full_name
-- FROM cards
-- JOIN users ON users.user_id=cards.user_id
-- JOIN trips ON cards.card_id=trips.card_id
-- GROUP BY trips.user_id, users.full_name
-- HAVING COUNT(cards.card_name) > 1;


-- 4
-- SELECT trip_id, trips.origin, trips.destination, users.full_name, cards.card_name, cards.charge
-- FROM trips
-- JOIN users ON users.user_id=trips.user_id
-- JOIN cards ON cards.card_id=trips.card_id;
