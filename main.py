import pygame
from datetime import datetime
import math

pygame.init()
display = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
center = (320,240)


while True:
    # get the current time
    time = datetime.strftime(datetime.now(), "%H:%M:%S")
    pygame.display.set_caption(time)
    display.fill((0,0,0))
    # outline of the clock
    pygame.draw.circle(display, (255,0,0), center, radius=200, width=5)
    # thing that holds the hands
    pygame.draw.circle(display, (255,0,0), center, 10)

    # get the time units
    hour = time[0:2]
    minutes = time[3:5]
    seconds = time[6:]

    # second hand
    s_angle_degrees = 6 * int(seconds)
    # need radians, adjust for starting point being pi/2
    s_angle_rad = (s_angle_degrees * math.pi / 180)
    # x and y coordinates for endpoint
    s_x = center[0] + 180 * math.sin(s_angle_rad)
    s_y = center[1] - 180 * math.cos(s_angle_rad) 
    # draw second hand
    pygame.draw.line(display, (0,0,255), center, (s_x, s_y), 1)

    # minute hand, accounting for smooth movement
    m_angle_degrees = 6 * int(minutes) + (6 * int(seconds) / 60)
    m_angle_rad = m_angle_degrees * math.pi / 180
    # coordinates
    m_x = center[0] + 180 * math.sin(m_angle_rad)
    m_y = center[1] - 180 * math.cos(m_angle_rad)
    # draw minute hand
    pygame.draw.line(display, (0,0,225), center, (m_x,m_y), 3)

    # hour hand
    h_angle_degrees = 30 * int(hour) + (30 * int(minutes) / 60)
    h_angle_rad = h_angle_degrees * math.pi / 180
    # coordinates
    h_x = center[0] + 150 * math.sin(h_angle_rad)
    h_y = center[1] - 150 * math.cos(h_angle_rad)
    # draw hour hand
    pygame.draw.line(display, (0,0,225), center, (h_x,h_y), 4)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()