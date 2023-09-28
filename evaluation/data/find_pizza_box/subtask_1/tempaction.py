def act(robot,env,camera):
    # Subtask 1: Open the Fridge
    fridge = registry(env, "fridge_xyejdx_0")
    open(rbot, fridge)
    donothing(env)

