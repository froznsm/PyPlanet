from pyplanet.apps.config import AppConfig
from pyplanet.apps.core.maniaplanet.callbacks.player import player_enter_player_slot, player_enter_spectator_slot


class ManiaplanetConfig(AppConfig):
	name = 'pyplanet.apps.core.maniaplanet'
	core = True

	async def on_start(self):
		self.context.signals.register_signal(player_enter_player_slot)
		self.context.signals.register_signal(player_enter_spectator_slot)
