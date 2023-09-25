def act(robot,env,camera):
    # Subtask 1: Open the fridge
    fridge = registry(env, "fridge_dszchb_0")
    open(roBot, fridge)
    donothing(env)

