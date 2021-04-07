_jaba_dict = {}


class Jaba:
    def __init__(self, my_jaba=None, gear=None):
        self.my_jaba = my_jaba
        self.gear = gear

    @staticmethod
    def set_my_jaba(person_id, my_jaba):
        jaba = Jaba._get_jaba(person_id)
        jaba.my_jaba = my_jaba
        Jaba._update_jaba(person_id, jaba)

    @staticmethod
    def set_gear(person_id, gear):
        jaba = Jaba._get_jaba(person_id)
        jaba.gear = gear
        Jaba._update_jaba(person_id, jaba)

    @staticmethod
    def get_full_info(person_id):
        jaba = Jaba._get_jaba(person_id)
        return f'{jaba.my_jaba}\n{jaba.gear}'

    @staticmethod
    def _get_jaba(person_id):
        if person_id not in _jaba_dict.keys():
            _jaba_dict[person_id] = Jaba()
        return _jaba_dict.get(person_id)

    @staticmethod
    def _update_jaba(person_id, jaba):
        _jaba_dict[person_id] = jaba
