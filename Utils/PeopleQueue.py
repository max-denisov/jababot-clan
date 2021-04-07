class PeopleQueue:
    def __init__(self):
        self._people = []

    def push(self, person_id):
        self._people.append(person_id)

    def pull(self):
        return self._people.pop(0)

    def size(self):
        return len(self._people)
