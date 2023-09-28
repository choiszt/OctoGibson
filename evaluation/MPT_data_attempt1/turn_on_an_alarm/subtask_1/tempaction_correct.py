

def act(robot, env, camera):
    fire_alert_142 = registry(env, 'fire_alarms_142')
    MoveBot(env, robot, fire_alert_142, camera)
    donothing(env)
