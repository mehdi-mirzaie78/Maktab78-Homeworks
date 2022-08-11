CREATE TABLE "cards"(
    "user id" INTEGER NOT NULL,
    "card id" INTEGER NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "charge" INTEGER NOT NULL,
    "expiration date" DATE NULL
);
ALTER TABLE
    "cards" ADD PRIMARY KEY("card id");
COMMENT
ON COLUMN
    "cards"."name" IS 'Only can be: single card - credit card - term card';
CREATE TABLE "bankaccount"(
    "user id" INTEGER NOT NULL,
    "Account id" INTEGER NOT NULL,
    "owner's name" VARCHAR(255) NOT NULL,
    "national code" VARCHAR(255) NOT NULL,
    "balance" INTEGER NOT NULL
);
ALTER TABLE
    "bankaccount" ADD PRIMARY KEY("Account id");
ALTER TABLE
    "bankaccount" ADD CONSTRAINT "bankaccount_national code_unique" UNIQUE("national code");
CREATE TABLE "users"(
    "user id" INTEGER NOT NULL,
    "full name" VARCHAR(255) NOT NULL,
    "age" INTEGER NOT NULL
);
ALTER TABLE
    "users" ADD PRIMARY KEY("user id");
CREATE TABLE "trips"(
    "user id" INTEGER NOT NULL,
    "trip id" INTEGER NOT NULL,
    "card id" INTEGER NOT NULL,
    "origin" VARCHAR(255) NOT NULL,
    "destination" VARCHAR(255) NOT NULL,
    "cost" INTEGER NOT NULL
);
ALTER TABLE
    "trips" ADD PRIMARY KEY("trip id");
ALTER TABLE
    "cards" ADD CONSTRAINT "cards_user id_foreign" FOREIGN KEY("user id") REFERENCES "users"("user id");
ALTER TABLE
    "trips" ADD CONSTRAINT "trips_card id_foreign" FOREIGN KEY("card id") REFERENCES "cards"("card id");
ALTER TABLE
    "bankaccount" ADD CONSTRAINT "bankaccount_user id_foreign" FOREIGN KEY("user id") REFERENCES "users"("user id");
ALTER TABLE
    "trips" ADD CONSTRAINT "trips_user id_foreign" FOREIGN KEY("user id") REFERENCES "users"("user id");





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

