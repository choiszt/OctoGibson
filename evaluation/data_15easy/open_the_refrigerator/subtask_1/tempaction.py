def act(robot,env,camera):
    # Subtask 1: Move therobot to the refrigerator
    fridge = registry(env, "fridge_xyejdx_0")
    MoveBot(env.get_env_topography, robot, fridge, camera)

