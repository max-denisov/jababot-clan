_people = []


class PeopleQueue:
    @staticmethod
    def push(person_id):
        _people.append(person_id)

    @staticmethod
    def pull():
        return _people.pop(0)

    @staticmethod
    def size():
        return len(_people)
