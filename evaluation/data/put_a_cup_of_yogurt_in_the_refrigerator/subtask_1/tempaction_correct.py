

def act(robot, env, camera):
    cup_85 = registry(env, 'cup_85')
    EasyGrasp(robot, cup_85)
    donothing(env)
