import math
from typing import List


class PhotoAlbum:
    def __init__(self, pages: int) -> None:
        self.pages = pages
        self.photos: List[List[str]] = self.__fill_matrix()
        self.curr_inx = 0

    def __fill_matrix(self) -> List[List[str]]:
        matrix = []
        for _ in range(self.pages):
            matrix.append([])
        return matrix

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count/4)
        return cls(pages)

    def add_photo(self, label: str):
        try:
            if len(self.photos[self.curr_inx]) == 4:
                self.curr_inx += 1
            self.photos[self.curr_inx].append(label)

            return f"{label} photo added successfully on page " \
                   f"{self.curr_inx + 1} slot " \
                   f"{len(self.photos[self.curr_inx])}"
        except IndexError:
            return "No more free slots"

    def display(self):
        result = "-" * 11 + "\n"
        for page in self.photos:
            result += " ".join("[]" for photo in page) + "\n"
            result += "-" * 11 + "\n"

        return result


# album = PhotoAlbum(2)
# 
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
# print(album.display())
