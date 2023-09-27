def act(robot,env,camera):
    # Subtask 6: Put the chocolates into the shopping cart
    shopping_cart = registry(env,"shopping_cart_kmgltg_1")
    chocolates = registry(env,"chocolates_177")
    put_inside(robot, chocolates, shopping_cart)
    donothing(env)

