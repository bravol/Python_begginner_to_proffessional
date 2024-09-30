enemies = 1

def increase_enemies():
    global enemies
    enemies += 2
    print(f"enemies inside function : {enemies}")

# global variables are available inside and outside functions
increase_enemies()
print(f"enemies outside function: {enemies} ")

# local scope
def drink_portion():
    portion_strength = 2
    print(portion_strength)



drink_portion()
# print(portion_strength)  cannot access a valuable inside the function


# player_health = 10
# # local
#  def game():
#      def drink_portion():
#          portion_strength = 2
#          print(player_health, portion_strength)
#
#      drink_portion()


game_level = 3
enemies = ["skeleton", "Zombie", "Alien"]

# block scope
def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)
#
# # global constants
# PI = 3.142
# def calc():
#     return 2 * PI