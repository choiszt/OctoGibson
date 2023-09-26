

def act(robot, env, camera):
    plastic_trash_can = registry(plastic_trash_can, 'plastic-trash-can-275')
    MoveBot(env, robot, plastic_trash_can, camera)
