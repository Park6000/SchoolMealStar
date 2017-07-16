

class school:
    def __init__(self, manuName):
        self.manuName = manuName
        self.allStar = 0
        self.allPeolpe = 0
        self.average = 0

    def allstar(self, star):
        self.allStar += int(star)
        self.allPeolpe = self.allPeolpe + 1
        print(self.manuName, self.allStar, self.allPeolpe)

    def average(self):
        if self.allPeolpe <= 0:
            print('투표자가 없습니다.')
            return None
        else:
            self.average = (self.allStar / self.allPeolpe)
            print('메뉴: %s, 별합: %s, 투표자: %s, 평균별점: %s' %(self.manuName, self.allStar, self.allPeolpe, round(self.average, 1)))