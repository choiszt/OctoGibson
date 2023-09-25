

def act(robot, env, camera):
    woredbaset = registry(env, "'worebasket_276'")
    EasyGrasp(robot, woredbaset)
    donothing(env)
