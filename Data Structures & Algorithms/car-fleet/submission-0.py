class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse = True)
        fleet = 0
        preTime = 0

        for pos,spd in cars:
            time = (target-pos)/spd

            if time>preTime:
                fleet += 1
                preTime = time
        return fleet

