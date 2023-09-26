def act(robot,env,camera):
    # Subtask 1: Open the stove
    stove = registry(env, "stove_rgpphy_0")
    open(roast, stove)
    donothing(env)

