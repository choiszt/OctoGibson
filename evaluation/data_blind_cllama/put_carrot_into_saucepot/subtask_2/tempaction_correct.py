

def act(robot, env, camera):
    carrot_178 = registry(env, 'carrot_178')
    EasyGrasp(robot, carrot_178)
    donothing(env)
