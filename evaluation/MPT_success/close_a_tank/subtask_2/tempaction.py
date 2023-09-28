def act(rotbot, env, camera):
  # Subask 2: Grasp TheTak
  tank_207 = registry (env,"tank-207")
  EasyGrasp(roBot, tank_207)
  donothing(env)
 
