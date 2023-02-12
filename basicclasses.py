class Seeds:
    def __init__(self, sowing_rate, ripeness_group, productivity_potential):
        self.sowing_rate = sowing_rate
        self.ripeness_group = ripeness_group
        self.productivity_potential = productivity_potential
    def __repr__(self):
        return f"This seed has: \n -sowing rate ->  {self.sowing_rate}\n" \
               f" -ripeness group: ->  {self.ripeness_group}\n" \
               f" -productivity potential ->  {self.productivity_potential}"


class CornSeeds(Seeds):
    def __init__(self, sowing_rate, ripeness_group, productivity_potential):
        super().__init__(sowing_rate, ripeness_group, productivity_potential)
        self.is_sugar = False
        self.fao_index = None


class SunflowerSeeds(Seeds):
    def __init__(self, sowing_rate, ripeness_group, productivity_potential):
        super().__init__(sowing_rate, ripeness_group, productivity_potential)
        self.express_technology = False
        self.oiliness = None


class WheatSeeds(Seeds):
    def __init__(self, sowing_rate, ripeness_group, productivity_potential):
        super().__init__(sowing_rate, ripeness_group, productivity_potential)
        self.winter_variety = False
        self.quality_class = None
