import time

import mujoco
import mujoco.viewer
import matplotlib.pyplot as plt



duration = 1000  # (seconds)

model = mujoco.MjModel.from_xml_path('scene_grid.xml')



data = mujoco.MjData(model)

viewer = mujoco.viewer.launch_passive(model,data)

viewer.cam.distance = model.stat.extent * 2

mujoco.mj_resetData(model, data)  # Reset state and time.




while data.time < duration:
    mujoco.mj_step(model, data)
    viewer.sync()

