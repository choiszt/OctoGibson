def act(robot,env,camera):
    # Subtask 1: Open the fridge
    fridge = registry(env,"fridge_xyejdx_0")
    open(robot, fridge)
    donothing(env)

