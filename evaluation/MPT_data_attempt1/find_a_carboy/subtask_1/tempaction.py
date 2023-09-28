def act(robot,env,camera):
    # Subtask 1: Move to The Reagent bottle (Reagent_Bottle)
    reagent = registry(env, "reagent-bottles_189")
    MoveBot(env.env, robot, reagent, camera)

