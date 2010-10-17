from planetwars.planet import Planet
from planetwars.player import PLAYER_MAP
from copy import copy
import player
import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
class Planet2(Planet):
    def in_future(self, turns=1):
        """Calculates state of planet in `turns' turns."""
        planet = copy(self)

        arriving_fleets = self.universe.find_fleets(destination=self)

        for i in range(1, turns+1):
            # account planet growth
            if planet.owner != player.NOBODY:
                planet.ship_count += self.growth_rate

            # get fleets which will arrive in that turn
            fleets = [ x for x in arriving_fleets if x.turns_remaining == i ]

            for fleet in fleets:
                if fleet.owner == planet.owner:
                    planet.ship_count += fleet.ship_count
                else:
                    planet.ship_count -= fleet.ship_count
                    if (planet.ship_count < 0):
                        planet.ship_count = -planet.ship_count
                        planet.owner = fleet.owner

        return planet
