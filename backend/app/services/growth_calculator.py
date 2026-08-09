class GrowthCalculator:
    
    @staticmethod
    def cagr(values):

        if values is None:

            return None

        if len(values) < 2:

            return None

        start = values[-1]

        end = values[0]

        years = len(values) - 1

        if start <= 0:

            return None

        cagr = (

            (end / start)

            ** (1 / years)

            - 1

        ) * 100

        return round(cagr, 2)

    @staticmethod
    def average_growth(values):

        if len(values) < 2:

            return None

        growth = []

        for i in range(len(values)-1):

            previous = values[i+1]

            current = values[i]

            if previous == 0:

                continue

            growth.append(

                (

                    (current-previous)

                    / previous

                )*100

            )

        if not growth:

            return None

        return round(

            sum(growth)

            / len(growth),

            2

        )