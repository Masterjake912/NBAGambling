def createTeamDict():
    team_dict = {1: "ATL",
                 2: "BOS",
                 3: "CLE",
                 4: "NOP",
                 5: "CHI",
                 6: "DAL",
                 7: "DEN",
                 8: "HOU",
                 9: "LAC",
                 10: "LAL",
                 11: "MIA",
                 12: "MIL",
                 13: "MIN",
                 14: "BKN",
                 15: "NYK",
                 16: "ORL",
                 17: "IND",
                 18: "PHI",
                 19: "PHX",
                 20: "POR",
                 21: "SAC",
                 22: "SAS",
                 23: "OKC",
                 24: "TOR",
                 25: "UTA",
                 26: "MEM",
                 27: "WAS",
                 28: "DET",
                 29: "CHA",
                 30: "GSW"}
    return team_dict

def printTeamAbbreviations():
    print("1. ATL")
    print("2. BOS")
    print("3. CLE")
    print("4. NOP")
    print("5. CHI")
    print("6. DAL")
    print("7. DEN")
    print("8. HOU")
    print("9. LAC")
    print("10. LAL")
    print("11. MIA")
    print("12. MIL")
    print("13. MIN")
    print("14. BKN")
    print("15. NYK")
    print("16. ORL")
    print("17. IND")
    print("18. PHI")
    print("19. PHX")
    print("20. POR")
    print("21. SAC")
    print("22. SAS")
    print("23. OKC")
    print("24. TOR")
    print("25. UTA")
    print("26. MEM")
    print("27. WAS")
    print("28. DET")
    print("29. CHA")
    print("30. GSW")


def main():
    team_dict = createTeamDict()
    print("Welcome to Jake's NBA Gambling BOT!")
    print("List of teams, Choose number correlating to team abbreviation:")
    printTeamAbbreviations()
    team1 = input("What is team 1? (Visiting Team) ")
    team2 = input("What is team 2? (Home Team) ")
    print(team_dict[int(team1)] + " @ " + team_dict[int(team2)])
    # printLineup(team1)
    # printLineup(team2)


if __name__ == "__main__":
    main()
