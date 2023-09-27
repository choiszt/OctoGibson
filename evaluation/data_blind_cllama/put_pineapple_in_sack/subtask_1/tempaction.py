def act(robot,env,camera):
    # Subtask 1: Move the robot to the grocery shelf where the pineapple is located.
    grocery_shelf_prtqlw_2 = registry(env, "grocery_shelf_prtqlw_2")
    MoveBot(env, robot, grocery_shelf_prtqlw_2, camera)
    donothing(env)

