

def act(robot, env, camera):
    trash_can = registry(trash_can, 'trash-can_79')
    MoveBot(env, robot, trash_can, camera)
    donothing(env)
