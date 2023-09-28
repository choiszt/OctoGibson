

def act(robot, env, camera):
    fridgesub = registry(env, 'fridgexyejdax_0', 'openable')
    open(robot, fridgesub)
    donothing(env)
