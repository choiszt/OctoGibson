def act(brobot,env,camera):
    # Subtask 1: Move to The Reagent(bott)pot:
    reagent bottle = registry(env, "reagentbottles_189")
    MoveBot(env.ooe_carrying_reagent, bottle, camera)
    donothing (env)

