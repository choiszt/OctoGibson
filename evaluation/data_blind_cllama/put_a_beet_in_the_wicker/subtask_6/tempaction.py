def act(robot,env,camera):
    # Subtask 2: Put the beet in the wicker basket
    beet = registry(env,"beet_277")
    wicker_basket = registry(env,"wicker_basket_276")
    put_inside(robot, beet, wicker_basket)
    donothing(env)

