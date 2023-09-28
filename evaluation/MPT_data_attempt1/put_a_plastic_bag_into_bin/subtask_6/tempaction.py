def act(rotbot, env, camera):
        # Sub task 2: Move to an object that is confirmed
        trash_can = registry(_task_goal,"trash-can_79")
        MoveBot(env, robot, trash_car, camera)
        donothing(env)
       

