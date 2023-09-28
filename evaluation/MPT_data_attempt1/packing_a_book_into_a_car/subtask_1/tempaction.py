def act(robot,env,camera):
    # Subtask 1: Move the bot to the case 
    case = registry(env, "case_188")
    MoveBot(env,"robot", case, camera)
    donothing(env)

