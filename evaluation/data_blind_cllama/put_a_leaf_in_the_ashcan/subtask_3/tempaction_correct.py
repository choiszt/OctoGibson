

def act(robot, env, camera):
    trash_can_281 = registry(env, 'trash_can_281')
    MoveBot(env, robot, trash_can_281, camera)
    donothing(env)
