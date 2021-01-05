from db.models.fact_creator import FactCreator


class ComparisonFactCreator(FactCreator):
    def __init__(self, creator: any, user_country: str, rival_country: str, exclude=None):
        # initialize language data
        FactCreator.__init__(self, creator=creator)
        self.user_country = user_country
        self.rival_country = rival_country
        if exclude is None:
            self.exclude = []
        else:
            self.exclude = exclude

    def create(self):
        if self.user_country in self.exclude or self.rival_country in self.exclude:
            return None
        return self.creator(self.user_country, self.rival_country)
