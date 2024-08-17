import matplotlib.pyplot as plt
import numpy as np
# Configuración del lienzo
size = 20
fig, ax = plt.subplots(1, 1, figsize = (size, size))


# Límites ejes
lim = 10
ax.set_xlim([-lim, lim])
ax.set_ylim([-lim, lim])


# Sol
sun_red = plt.Circle(xy = (10, 10), radius = 5, color = "#FF4500", alpha = 0.4)
sun_orange = plt.Circle((10, 10), 4, color = "#FF7F00", alpha = 0.3)
sun_yellow = plt.Circle((10, 10), 3, color = "#FFD700", alpha = 0.2)
ax.add_artist(sun_red)
ax.add_artist(sun_orange)
ax.add_artist(sun_yellow)


# Pyratilla
# * cuerpo
body = plt.Circle((-3, -4.5), 1, color = "#FF6A6A")
ax.add_artist(body)
# * espada
sword_edge_points = np.array([[-1.35, -3.85], [-1.6, -3.6], [-0.8, -2.8], 
                              [-0.4, -2.65], [-0.55, -3.05]])
sword_handle_points = np.array([[-1.85, -3.35], [-2.05, -3.55], [-1.8, -3.8], [-2, -4], 
                         [-1.75, -4.25], [-1.55, -4.05], [-1.3, -4.3], [-1.1, -4.1],
                         [-1.35, -3.85], [-1.6, -3.6]])
sword_edge = plt.Polygon(sword_edge_points, color = "#E0E0E0")
sword_handle = plt.Polygon(sword_handle_points, color = "#8F8F8F")
ax.add_artist(sword_edge)
ax.add_artist(sword_handle)
# * cabeza
head = plt.Circle((-3, -3), 0.8, color = "#FF6A6A")
eye_right = plt.Circle((-2.7, -2.8), 0.2, color = "#FFFFFF")
eye_pupil_right = plt.Circle((-2.7, -2.8), 0.1, color = "#000000")
eye_left = plt.Circle((-3.3, -2.8), 0.2, color = "#FFFFFF")
eye_pupil_left = plt.Circle((-3.3, -2.8), 0.1, color = "#000000")
ax.add_artist(head)
ax.add_artist(eye_right)
ax.add_artist(eye_pupil_right)
ax.add_artist(eye_left)
ax.add_artist(eye_pupil_left)
# * sombrero
hat_points = np.array([[-2, -2.5], [-2, -2.2], [-2.3, -2.2], [-2.3, -1.7], [-2.6, -1.4],
                       [-3.4, -1.4], [-3.7, -1.7], [-3.7, -2.2], [-4, -2.2], [-4, -2.5]])
hat = plt.Polygon(hat_points, color = "#000000")
ax.add_artist(hat)


# Barco
# * base
boat_points = np.array([[-8, -8], [-2, -8], [-1, -5], [-9, -5]])
boat_bottom_points = np.array([[-8, -8], [-2, -8], [-1.5, -6.5], [-8.5, -6.5]])
boat = plt.Polygon(boat_points, color = "#CD853F")
boat_bottom = plt.Polygon(boat_bottom_points, color = "#8B5A2B", alpha = 0.3)
ax.add_artist(boat)
ax.add_artist(boat_bottom)
# * vela
mast_points = np.array([[-4.8, -5], [-5.2, -5], [-5.2, 5], [-4.8, 5]])
sail_points = np.array([[-5.2, 4.5], [-5.2, -2.5], [-9, 0]])
mast = plt.Polygon(mast_points, color = "#FFC125", fill = False)
sail = plt.Polygon(sail_points, color = "#FFC1C1", fill = False, lw = 2)
ax.add_artist(mast)
ax.add_artist(sail)


# Enemigo
# * cuerpo
enemy_body_points = np.array([[2.5, -8], [7.5, -8], [7.5, -3], [2.5, -3]])
enemy_body = plt.Polygon(enemy_body_points, color = "#00CD00")
ax.add_artist(enemy_body)
# * boca
enemy_mouth_points = np.array([[6.5, -7.5], [3.5, -7.5], [3.5, -5.5], [6.5, -5.5]])
enemy_teeth_points = np.array([[3.5, -5.5], [4, -6], [4.5, -5.5], [5, -6], [5.5, -5.5], [6, -6], [6.5, -5.5]])
enemy_mouth = plt.Polygon(enemy_mouth_points, color = "#000000")
enemy_teeth = plt.Polygon(enemy_teeth_points, color = "#FFFFFF")
ax.add_artist(enemy_mouth)
ax.add_artist(enemy_teeth)
# * ojos
enemy_eyes_points = np.array([[3.5, -3.3], [4.5, -4.3], [3.5, -5.3], [6.5, -3.3], [5.5, -4.3], [6.5, -5.3]])
enemy_eye_left = plt.Polygon(enemy_eyes_points[:3, :], color = "#FF4040")
enemy_eye_right = plt.Polygon(enemy_eyes_points[3:, :], color = "#FF4040")
ax.add_artist(enemy_eye_left)
ax.add_artist(enemy_eye_right)


# Olas
waves_x = np.linspace(-lim, lim, 400)
# * olas bajas
ax.plot(waves_x, np.sin(waves_x) - lim, color = "#000080")
ax.plot(waves_x, np.cos(waves_x) - lim, color = "#00CDCD")
# * olas medias
ax.plot(waves_x, np.sin(waves_x) - lim + 1, color = "#0000CD")
ax.plot(waves_x, np.cos(waves_x) - lim + 1, color = "#00EEEE")
# * olas altas
ax.plot(waves_x, np.sin(waves_x) - lim + 2, color = "#0000FF")
ax.plot(waves_x, np.cos(waves_x) - lim + 2, color = "#00FFFF")


plt.show()