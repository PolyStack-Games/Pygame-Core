def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

def wrap_around_screen(rect, screen_width, screen_height):
    if rect.left > screen_width:
        rect.right = 0
    elif rect.right < 0:
        rect.left = screen_width
    if rect.top > screen_height:
        rect.bottom = 0
    elif rect.bottom < 0:
        rect.top = screen_height
