

def act(robot, env, camera):
    reagentpot = registry(env, "'reagentpot_192'")
    EasyGrasp(robot, reagentpot)
    donothing(env)
