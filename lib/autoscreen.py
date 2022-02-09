import time

try:
    from typing import Optional, Callable
except ImportError:
    pass


class AutoOffScreen:
    def __init__(self, duration=60 * 15, initial_duration=10) -> None:
        self.on = True
        # Current on/off status

        self._turn_off = None  # type: Optional[int]
        # Scheduled time to turn off

        self.duration = duration
        # Duration to stay on after being activated

        self.set_turn_off(time.monotonic() + initial_duration)

        self.handle_on = None  # type: Optional[Callable[[],None]]
        # Function called when we should turn on."""

        self.handle_off = None  # type: Optional[Callable[[],None]]
        # Function called when we should turn off.

        self._last_on = False

    def set_turn_off(self, off_time):
        self.on = True
        if self._turn_off:
            self._turn_off = max(self._turn_off, off_time)
        else:
            self._turn_off = off_time

    def update_active(self):
        """turn on/push out turn-off time"""
        self.set_turn_off(time.monotonic() + self.duration)

    def poll(self) -> bool:
        was_on = self.on
        now = time.monotonic()
        if self.on and self._turn_off is not None and now >= self._turn_off:
            self.on = False
            self._turn_off = None
        if self._last_on != self.on:
            if self.on and self.handle_on is not None:
                self.handle_on()
            if not self.on and self.handle_off is not None:
                self.handle_off()
        self._last_on = self.on
        return self.on