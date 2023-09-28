def act(robbot, env, camera):
  # Subask 2: Move to theplastic recyclebin
  plastic_trash_can = registry (task_goal,"plastic-trash-can-275")
  MoveBot (env, robot, plastic_trask_can, camera)

