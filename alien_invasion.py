import sys
import  pygame
from random import randint
from settings.settings import Settings
from Models.ship import Ship
from Models.bullet import Bullet
from Models.alien import Alien

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings =Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Aline Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        
    def run_game(self):#main loop game
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blime()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)

        pygame.display.flip()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien.
        alien = Alien(self)
        self.aliens.add(alien)

        alien_width, alien_height = alien.rect.size
        # Spacing between each alien is equal to one alien width.
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        self._create_fleet_type_formation(1,number_aliens_x,number_rows)

    def _create_fleet_type_formation(self, type,number_aliens_x_avirable, number_rows_avirable):
        if type ==1:
            for row_number in range(number_rows_avirable):
                # Create the first row of aliens.
                for alien_number in range(number_aliens_x_avirable):
                    # Create an alien and place it in the row.
                    alien = Alien(self)
                    alien_width, alien_height = alien.rect.size
                    alien.rect.x = alien_width + 2 * alien_width * alien_number
                    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
                    alien.x = float(alien.rect.x)
                    self.aliens.add(alien)
        elif type ==2:
            for alien_number in range(number_aliens_x_avirable):
                alien = Alien(self)
                alien.rect.x = alien.rect.width + 2 * alien.rect.width * alien_number
                alien.x = float(alien.rect.x)
                self.aliens.add(alien)
        elif type ==3:
            random_number=2
            for row_number in range(number_rows_avirable):
                # Create the first row of aliens.
                for alien_number in range(number_aliens_x_avirable):
                    random_number= randint(0, 1)
                    if random_number == 1:
                        # Create an alien and place it in the row.
                        alien = Alien(self)
                        alien_width, alien_height = alien.rect.size
                        alien.rect.x = alien_width + 2 * alien_width * alien_number
                        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
                        alien.x = float(alien.rect.x)
                        self.aliens.add(alien)
        #elif type ==4:
        #    None
        #elif type ==5:
        #    None
    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()
    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
            break
            
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
            self.settings.fleet_direction *= -1

if __name__ == '__main__':
    gameAi = AlienInvasion()
    gameAi.run_game()