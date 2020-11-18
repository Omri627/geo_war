from analyzers.dict_analyzer import DictAnalyzer


class CountriesDictAnalyzer(DictAnalyzer):

    def analyze_dict(self, raw_data: dict) -> None:
        data = dict()
        data['code'] = raw_data['code']
        data['name'] = raw_data['name']
        data['area'] = float(raw_data['geography']['area']['total'].split()[0])
        data['population'] = int(raw_data['people_and_society']['population'].split()[0].replace(',', ''))
        data['nationality'] = raw_data['people_and_society']['nationality']['adjective'].split(",")[0]
        data['birth_rate'] = float(raw_data['people_and_society']['birth_rate'].split()[0])
        data['death_rate'] = float(raw_data['people_and_society']['death_rate'].split()[0])
        data['cellular_subscriptions'] = int(
            raw_data['communications']['telephones_mobile_cellular']['total_subscriptions'].replace(',', ''))
        print(data)
