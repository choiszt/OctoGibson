def act(robot,env,camera):
    # Subtask 2: Open the fridge
    fridge = registry(env,"fridge_xyejdx_0")
    open(robot, fridge)
    donothing(env)

