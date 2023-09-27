def act(task,robot):
  # Subtail 1: Moveto The Recycling_bin
  recycling_bin = registry (env,'recyclING_bin-188')
  MoveBot(env.world, robot, recycling_ bin, camera)
  donothing (env)

