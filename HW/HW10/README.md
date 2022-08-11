### Homework 10

-------------------
+ #### HW10-1:
  - Indenter class context manager.
+ #### HW10-2:
  - Generator for determining is a number, armstrong number.
+ #### HW10-3:
  - Decorator process timer & cache for fibonacci & factorial functions.
+ #### HW10-4:
  - Query codes for subway project
  
    1- First I created new ERD.
      <img src=https://github.com/mehdi-mirzaie78/Maktab78-Homeworks/blob/main/HW/HW10/Pictures/ERD.png width="800" height="550">
  
    2- I created a database with some data to work with.
    
    3- I wrote appropriate queries to see the asked results.

```sql
-- 1
SELECT DISTINCT trips.user_id, users.full_name
FROM trips
JOIN users
ON users.user_id=trips.user_id;
```

![]("https://github.com/mehdi-mirzaie78/Maktab78-Homeworks/blob/main/HW/HW10/Pictures/1.png")

---

```sql
-- 2
SELECT DISTINCT trips.user_id, trip_id, users.full_name, cards.card_name
FROM trips
JOIN users
ON users.user_id=trips.user_id
JOIN cards ON cards.card_id=trips.card_id
WHERE cards.card_name='single';
```
![]("https://github.com/mehdi-mirzaie78/Maktab78-Homeworks/blob/main/HW/HW10/Pictures/2.png")

---

```sql
-- 3
SELECT COUNT(cards.card_name) AS number_of_card_used, trips.user_id, users.full_name
FROM cards
JOIN users ON users.user_id=cards.user_id
JOIN trips ON cards.card_id=trips.card_id
GROUP BY trips.user_id, users.full_name
HAVING COUNT(cards.card_name) > 1;
```
![]("https://github.com/mehdi-mirzaie78/Maktab78-Homeworks/blob/main/HW/HW10/Pictures/3.png")

---

```sql
-- 4
SELECT trip_id, trips.origin, trips.destination, users.full_name, cards.card_name, cards.charge
FROM trips
JOIN users ON users.user_id=trips.user_id
JOIN cards ON cards.card_id=trips.card_id
ORDER BY trip_id ASC;
```
![]("https://github.com/mehdi-mirzaie78/Maktab78-Homeworks/blob/main/HW/HW10/Pictures/4.png")


