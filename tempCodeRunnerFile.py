# End game if player runs out of lives
if lives == 0:
    game_over = True

# Draw game objects
screen.fill((255, 255, 255))
screen.blit(basket.image, basket.rect)
for fruit in fruits:
    screen.blit(fruit.image, fruit.rect)
font = pygame.font.SysFont("Arial", 30)
score_text = font.render("Score: " + str(score), True, (0, 0, 0))
lives_text = font.render("Lives: " + str(lives), True, (0, 0, 0))
screen.blit(score_text, (10, 10))
screen.blit(lives_text, (SCREEN_WIDTH - lives_text.get_width() - 10, 10))

# Flip display buffer
pygame.display.flip()

# Control frame rate
clock.tick(60)
