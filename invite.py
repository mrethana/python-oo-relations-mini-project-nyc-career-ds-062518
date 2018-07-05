class Invite:

    _all = []

    def __init__(self, dinner_party, guest, rsvp_status = None):
        self._dinner_party = dinner_party
        self._guest = guest
        self._rsvp_status = rsvp_status
        Invite._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @property
    def guest(self):
        return self._guest

    @guest.setter
    def guest(self, guest):
        self._guest = guest

    @property
    def dinner_party(self):
        return self._dinner_party

    @dinner_party.setter
    def dinner_party(self, dinner_party):
            self._dinner_party = dinner_party

    @property
    def resvp_status(self):
        return self._resvp_status

    @resvp_status.setter
    def resvp_status(self, resvp_status):
        self._resvp_status = resvp_status

    def accepted(self):
        return self._rsvp_status

    # @property
    # def accepted(self):
    #     return self._accepted
    #
    # @accepted.setter
    # def accepted(self, accepted):
    #     self._accepted = accepted
