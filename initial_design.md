# Initial Design Document
#### PLEASE! PLEASE! PLEASE! READ the [README.md](README.md) File carefully
1. write a function named play
   1. set variable sticks to ask how many sticks are used in the game(10-100)
   2. set variable player to equal 1
   3. while sticks > 0:
      1. output whose turn it is
      2. if player equals 3:
         3. set computer sticks to a random number 1-3 that the computer picks
         4. set sticks to sticks minus computer sticks
         5. output how many sticks the computer picks
         6. set player to 1
      3. if players equals 1 or 2:
         2. ask how many sticks the player wants to take
         3. while sticks are less than 1 and greater than 3:
            1. output "must choose between 1-3"
            2. output "how many sticks do you want to take"
         4. subtract the amount of sticks taken from sticks
         5. set player to player + 1
         6. if player is greater than 3:
            1. player equals 1
   4. set player to player - 1
   5. if player equals 0:
      1. player equals 3
   6. output "Game over player(_) lost"
2. invoke function play
3. ask if user wants to play again
4. if user says yes:
   5. invoke function play
5. if user says no:
   6. output "thank you for playing"
6. otherwise:
   7. output "must inout yes or no"
    