def act(robot,env,camera):
    # Subtask 1: Move to bottom grocery shelves.
    bottom_grocery_shelf = registry(env, "bottom_cycling_groove_86")
    MoveBot(env, robot, bottom_groceryshelf, camera)
    donothing(env)

