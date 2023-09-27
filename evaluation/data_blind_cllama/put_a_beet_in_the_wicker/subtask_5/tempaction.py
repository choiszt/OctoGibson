def act(robot,env,camera):
    # Subtask 1: Move the robot to the wicker basket
    wicker_basket = registry(env,"wicker_basket_276")
    MoveBot(env, robot, wicker_basket, camera)
    donothing(env)

