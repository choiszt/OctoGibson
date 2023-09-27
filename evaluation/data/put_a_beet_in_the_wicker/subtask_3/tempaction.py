def act(robot,env,camera):
    # Subtask 3: Find the wicker basket
    wicker_basket = registry(env,"wicker_basket")
    # Since the wicker basket is not observed in the environment, we need to move the robot around to find it.
    # Here we assume that the wicker basket is placed directly on the ground, so we can use the MoveBot function to move the robot.
    # We also assume that the wicker basket is not too far away from the robot, so we can use the shortest path to move the robot to the wicker basket.
    MoveBot(env, robot, wicker_basket, camera)
    donothing(env)

