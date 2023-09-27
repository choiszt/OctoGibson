

def act(robot, env, camera):
    money_142 = registry(env, 'money_142')
    MoveBot(env, robot, money_142, camera)
    donothing(env)
