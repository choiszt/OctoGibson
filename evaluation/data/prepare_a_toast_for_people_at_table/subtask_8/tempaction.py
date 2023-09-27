def act(robot,env):
    # Subtop:
    countertop=registry(env,"countertop-tpuwsys_1")
    MoveBot (env, robot.is_nextto(countertop), camera) 
    donothing (env)

