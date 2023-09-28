def act(robot,env,camera):
    # Subtask 1: Open the refrigerator
    fridge = registry(env, "fridge_xyejdx_0")
    open(root, fridge)
    donothing(env)

