# ERD Explanation
___
+ __Card__
  + We have a class of Card which includes :(single trip, credit, term). 
  + Each card has a name and amount of charge, but only term card has expiration date.
  + We have a method for charging cards and a method to pay the cost of the trip.
+ __Bank Account__
  + We have a class of Bank Account for the class of User
  in Bank Account class we can withdraw and deposit transaction.

+ __User__
  + We have a user who has a bank account with his/her information, and it's possible to do finance transactions.
  + Our user can purchase cards for trip

+ __Trip__
  + In Trip class we have origin, destination, user, and a card which our user will pay the cost with it.
