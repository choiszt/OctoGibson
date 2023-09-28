def act(robot, env, camera):
  # Subtask 1: Move the Robot to the Shoppingcart.         
  shopping_cart_kmgltg_1 = registry(env, "shooping_cart(kmgltyg_1")
  MoveBot(env, robot, shopping_cart, camera)
  donothing(env)

