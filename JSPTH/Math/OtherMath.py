import math

class AngleConverter:
    units_in_radians = {
        'radian': 1,
        'degree': math.pi / 180,
        'gradian': math.pi / 200,
    }

    @staticmethod
    def convert_angle(value, from_unit, to_unit):
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        if from_unit not in AngleConverter.units_in_radians or to_unit not in AngleConverter.units_in_radians:
            raise ValueError(f"Unsupported unit: {from_unit} or {to_unit}")

        value_in_radians = value * AngleConverter.units_in_radians[from_unit]
        return value_in_radians / AngleConverter.units_in_radians[to_unit]
