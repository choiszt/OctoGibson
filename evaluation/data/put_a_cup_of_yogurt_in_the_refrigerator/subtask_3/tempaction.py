def act(ribot, env):
    # Subtask 3: Move to The fridge,Open The fridge 4.
    fridge = registry(env, "fridge_xyejdx_0")
    MoveBot(env.camera, robot, fridge, camera)
    donothing(env)

