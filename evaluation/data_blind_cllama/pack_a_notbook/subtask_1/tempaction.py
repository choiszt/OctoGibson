def act(robot,env,camera):
    # Subtask 1: Move the robot to the grocery shelf
    grocery_shelf = registry(env, "grocery_shelf_prtqlw_1")
    MoveBot(env, robot, grocery_shelf, camera)
    donothing(env)

