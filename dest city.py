
class Solution(object):
    def destCity(self, paths):
        startCitySet = set([path[0] for path in paths])
        destCitySet = set([path[1] for path in paths])

        # We can subtract one set from another and it will
        # give us only the elements that are not present
        # in the second set
        cityWithNoDestination = destCitySet - startCitySet 

        return cityWithNoDestination.pop()


class Solution(object):
    def destCity(self, paths):
        startCitySet = set([path[0] for path in paths])
        destCitySet = set([path[1] for path in paths])

        destinationCity = destCitySet - startCitySet

        return destinationCity.pop()