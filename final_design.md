# Final Design Document
#### PLEASE! PLEASE! PLEASE! Complete all the NOs in the feedback document 
1. write a function named play
   1. set variable sticks to ask how many sticks are used in the game(10-100)
   2. set variable player to equal 1
   3. while sticks > 0:
      1. output whose turn it is
      2. if player equals player three:
         1. set computer sticks to a random number 1-3 that the computer picks
         2. if sticks are less than 3 
            1. set computer sticks to a random number 1-2
         3. otherwise if sticks are less than 2
            1. set computer sticks to 1
         4. set sticks to sticks minus computer sticks
         5. output how many sticks the computer picks
         6. set player to player one
      3. if players equals 1 or 2:
         1. ask how many sticks the player wants to take
         2. while sticks are less than 1 and greater than 3:
            1. output "must choose between 1-3"
            2. output "how many sticks do you want to take"
         3. subtract the amount of sticks taken from sticks
         4. set player to player + 1
         5. if player is greater than 3:
            1. player equals 1
   4. set player to player - 1
   5. if player equals 0:
      1. player equals 3
   6. output "Game over player(_) lost"
   7. set loses to 0
   8. if sticks equal 0:
      1. player_lose = player
      2. add 1 to loses
      3. output how many loses the player has
2. invoke function play
3. ask if user wants to play again
4. while user says yes:
   1. invoke function play
   2. ask if user wants to play again
5. if user says no:
   1. output "thank you for playing"
6. otherwise:
   1. output "must inout yes or no"