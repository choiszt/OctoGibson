

def act(robot, env, camera):
    box_of_chocolates = registry(env, 'box_of_chocolates_143')
    EasyGrasp(robot, box_of_chocolates)
    donothing(env)
