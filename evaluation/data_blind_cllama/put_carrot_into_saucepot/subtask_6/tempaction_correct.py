

def act(robot, env, camera):
    carrot_151 = registry(env, 'carrot_151')
    saucepot_170 = registry(env, 'saucepot_170')
    unfold(robot, carrot_151, saucepot_170)
    donothing(env)
