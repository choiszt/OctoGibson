

def act(robot, env, camera):
    chocolates = registry(env, 'chocolates_177')
    EasyGrasp(robot, chocolates)
    donothing(env)
