from typing import List

from project.room import Room


class Hotel:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        room = next(filter(lambda x: x.number == room_number, self.rooms))

        if not room.is_taken:
            if people <= room.capacity:
                room.is_taken = True
                self.guests += people

    def free_room(self, room_number: int) -> None:
        room = next(filter(lambda x: x.number == room_number, self.rooms))

        if room.is_taken:
            room.is_taken = False
            self.guests = 0

    def status(self) -> str:
        free_rooms_numbers = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms_numbers = [str(r.number) for r in self.rooms if r.is_taken]

        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(free_rooms_numbers)}\n" \
               f"Taken rooms: {', '.join(taken_rooms_numbers)}"








