import pygame
import math

class JarvisVisual():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    width, height = 400, 400
    screen = pygame.display.set_mode((width, height))
    icon = pygame.image.load("jarv.jpg")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Jarvis")

    # Colors
    BLACK = (0, 0, 0)

    # Main game loop
    running = True
    angle1 = 0
    angle3 = 90  # Angle offset for the third line

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill(BLACK)

        # Calculate the position of the first spinning line
        radius1 = 100
        center_x, center_y = width // 2, height // 2
        line_length1 = 120  # Length of the first curved line segment

        # Calculate the start and end angles of the first curved line segment
        start_angle1 = math.radians(angle1)
        end_angle1 = math.radians(angle1 + 90)

        # Calculate the color for the first curved line segment
        color1 = pygame.Color(255, 0, 0)
        color1.hsla = (angle1 % 360, 100, 50, 100)

        # Draw the first spinning curved line segment
        pygame.draw.arc(screen, color1, (center_x - radius1, center_y - radius1, radius1 * 2, radius1 * 2), start_angle1, end_angle1, 4)

        # Calculate the position of the second spinning line
        radius2 = 150
        line_length2 = 180  # Length of the second curved line segment

        # Calculate the start and end angles of the second curved line segment
        start_angle2 = math.radians(-angle1)
        end_angle2 = math.radians(-angle1 - 90)

        # Calculate the color for the second curved line segment
        color2 = pygame.Color(255, 0, 0)
        color2.hsla = ((angle1 + 180) % 360, 100, 50, 100)

        # Draw the second spinning curved line segment
        pygame.draw.arc(screen, color2, (center_x - radius2, center_y - radius2, radius2 * 2, radius2 * 2), start_angle2, end_angle2, 6)

        # Calculate the position of the third spinning line
        radius3 = 200
        line_length3 = 240  # Length of the third curved line segment

        # Calculate the start and end angles of the third curved line segment
        start_angle3 = math.radians(angle3)
        end_angle3 = math.radians(angle3 + 90)

        # Calculate the color for the third curved line segment
        color3 = pygame.Color(255, 0, 0)
        color3.hsla = ((angle3 + 90) % 360, 100, 50, 100)

        # Draw the third spinning curved line segment
        pygame.draw.arc(screen, color3, (center_x - radius3, center_y - radius3, radius3 * 2, radius3 * 2), start_angle3, end_angle3, 8)

        # Update the angles
        angle1 += 1
        angle3 += 1.5

        # Update the display
        pygame.display.flip()

        # Delay between frames (5 milliseconds in this case)
        pygame.time.delay(5)

    # Quit Pygame
    pygame.quit()