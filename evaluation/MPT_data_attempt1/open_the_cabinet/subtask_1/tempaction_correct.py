

def act(robot, env, camera):
    cabintask_94 = registry(env, 'cabin_task_94')
    MoveBot(env, robot, cabintask_94, camera)
    donothing(env)
