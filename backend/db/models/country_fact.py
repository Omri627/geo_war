from db.models.fact_creator import FactCreator


class CountryFactCreator(FactCreator):
    def __init__(self, creator: any, country: str, real_or_fake: bool, exclude=None):
        # initialize language data
        FactCreator.__init__(self, creator=creator)
        self.country = country
        self.real_or_fake = real_or_fake
        if exclude is None:
            self.exclude = []
        else:
            self.exclude = exclude

    def create(self):
        if self.country in self.exclude:
            return None
        return self.creator(self.country, self.real_or_fake)
