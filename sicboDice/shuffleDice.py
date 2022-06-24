import random

class SicboDice():
    __doubleWithOneDice = "113-114-115-116-221-223-224-225-226-331-332-334-335-336-441-442-443-445-446-551-552-553-554-556-661-662-663-664"
    __tripleCombineDice = "126-135-234-256-346-123-136-145-235-356-124-146-236-245-456-125-134-156-246-345"
    __twoCombineDice = "12-13-14-15-16-23-24-25-26-34-35-36-45-46-56"
    __threeDiceFromFourPossibleCombinations = ["1234", "2345", "2356", "3456"]

    def __shuffleDice(self):

        #random
        diceRandom1 = [1, 4, 6, 3, 2, 5]

        diceRandom2 = [6, 1, 2, 4, 5, 3]

        diceRandom5 = [4, 3, 1, 5, 6, 2]

        diceRandom3 = [5, 2, 4, 1, 3, 6]

        diceRandom6 = [3, 6, 5, 2, 1, 4]
        
        diceRandom4 = [2, 5, 3, 6, 4, 1]
        
        listRD = [diceRandom1, diceRandom2, diceRandom3, diceRandom4, diceRandom5, diceRandom6]
        
        random.shuffle(listRD)
        shake = [listRD[random.randint(0, 1)][random.randint(0, 5)], listRD[random.randint(2, 3)][random.randint(0, 5)], listRD[random.randint(4, 5)][random.randint(0, 5)]]

        return shake

    def __checkTriple(self, dice):
        result = None
        if dice[0] == dice[1] and dice[0] == dice[2]:
            result = dice[0]
        return result
    
    def __checkDouble(self, dice):
        result = None

        if dice[0] == dice[1] or dice[0] == dice[2]:
            result = dice[0]

        if dice[1] == dice[2]:
            result = dice[1]

        return result

    def __checkSmallBig(self, tot):
        if tot <= 10:
            return 0
        else:
            return 1

    def __checkOddEven(self, tot):
        if tot%2 == 1:
            return 1
        else:
            return 0
    
    def __checkDoubleWithOneDice(self, sortDice, revSortDice):
        result = None

        strSortDice = str(sortDice[0])+str(sortDice[1])+str(sortDice[2])
        strRevSortDice = str(revSortDice[0])+str(revSortDice[1])+str(revSortDice[2])

        if self.__doubleWithOneDice.find(strSortDice) != -1:
            result = strSortDice
        
        if self.__doubleWithOneDice.find(strRevSortDice) != -1:
            result = strRevSortDice
        
        return result

    def __checkTripleCombineDice(self, dice):
        result = None

        strDice = str(dice[0])+str(dice[1])+str(dice[2])
        
        if self.__tripleCombineDice.find(strDice) != -1:
            result = strDice
        
        return result

    def __checkThreeDiceFromFourPossibleCombinations(self, dice):
        result = []

        for combine in self.__threeDiceFromFourPossibleCombinations:
            count = 0
            if combine.find(str(dice[0])) != -1:
                count += 1

            if combine.find(str(dice[1])) != -1:
                count += 1

            if combine.find(str(dice[2])) != -1:
                count += 1
            
            if count == 3:
                result.append(combine)
        
        if len(result) == 0:
            result = None
        
        return result
    
    def __checkTwoCombineDice(self, dice):
        result = []

        strDice01 = str(dice[0])+str(dice[1])
        strDice02 = str(dice[0])+str(dice[2])
        strDice12 = str(dice[1])+str(dice[2])
        
        if self.__twoCombineDice.find(strDice01) != -1:
            if strDice01 not in result:
                result.append(strDice01)
        
        if self.__twoCombineDice.find(strDice02) != -1:
            if strDice02 not in result:
                result.append(strDice02)
        
        if self.__twoCombineDice.find(strDice12) != -1:
            if strDice12 not in result:
                result.append(strDice12)
        
        if len(result) == 0:
            result = None
        
        return result

    def getDice(self):
        """
        This function will determine the results of shuffling the dice that will be used in the Sicbo game.
        """
        try:
            dice = self.__shuffleDice()
            
            sortDice = sorted(dice)
            revSortDice = sorted(dice, reverse=True)
            totDice = sum(dice) if (sum(dice) != 3 or sum(dice) != 18) else None
            triple = self.__checkTriple(dice)
            double = self.__checkDouble(dice) if  triple == None else triple
            BS = self.__checkSmallBig(totDice) if  (triple == None) else None
            OE = self.__checkOddEven(totDice) if  triple == None else None
            doubleWithOneDice = self.__checkDoubleWithOneDice(sortDice, revSortDice) if (double != None and triple == None) else None
            tripleCombineDice = self.__checkTripleCombineDice(sortDice) if (double == None and triple == None) else None
            threeDiceFromFourPossibleCombinations = self.__checkThreeDiceFromFourPossibleCombinations(sortDice) if (double == None and triple == None) else None
            twoCombineDice = self.__checkTwoCombineDice(sortDice) if (triple == None) else None
            
            return  {
                "dice": dice,
                "total": totDice,
                "triple": triple,
                "double": double,
                "isBig": BS,
                "isOdd": OE,
                "doubleWithOneDice": doubleWithOneDice,
                "tripleCombineDice": tripleCombineDice,
                "twoCombineDice": twoCombineDice,
                "threeDiceFromFourPossibleCombinations" : threeDiceFromFourPossibleCombinations
            }

        except Exception as e:
            print(e +'\n')
