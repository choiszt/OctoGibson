

def act(robot, env, camera):
    carrot = registry(env, 'carrot')
    EasyGrasp(robot, carrot)
    donothing(env)
