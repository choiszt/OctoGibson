def act(robot,env,camera):
    # Subtask 1: Move the Robot from the Grocery_Shelf_PRtQLw_ 0 to the Shopping_Cart_KmglTg_ 1
    grocery_shelfs = registry(env, "groccoli_s_sjmdri_0")
    shopping_cart = registry (env, "'shopper_cart'")

