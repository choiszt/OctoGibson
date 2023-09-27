

def act(robot, env, camera):
    shopping_cart = registry(env, 'shopping_cart_kmgltg_1')
    chocolates = registry(env, 'chocolates_177')
    unfold(robot, chocolates, shopping_cart)
    donothing(env)
