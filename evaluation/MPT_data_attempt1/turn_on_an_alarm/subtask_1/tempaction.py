def act(robot,env,camera):
    # Subtask 1: Move The robot to The Fire Alarm
    fire_alert_142 = registry(env,"fire_alarms_142")
    MoveBot(env, robot, fire_alert, camera)
    donothing(env)

