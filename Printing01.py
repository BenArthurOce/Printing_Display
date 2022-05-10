val = 10
match val:
    case 1:
        ## Python program to print the data
        d = {1: ["Python", 33.2, 'UP'],
        2: ["Java", 23.54, 'DOWN'],
        3: ["Ruby", 17.22, 'UP'],
        10: ["Lua", 10.55, 'DOWN'],
        5: ["Groovy", 9.22, 'DOWN'],
        6: ["C", 1.55, 'UP']
        } 
        print ("Pos,Lang,Percent,Change")
        for k, v in d.items():
            lang, perc, change = v
            print (k, lang, perc, change)

    case 2:
        ## Python program to print the data
        d = {1: ["Python", 33.2, 'UP'],
        2: ["Java", 23.54, 'DOWN'],
        3: ["Ruby", 17.22, 'UP'],
        10: ["Lua", 10.55, 'DOWN'],
        5: ["Groovy", 9.22, 'DOWN'],
        6: ["C", 1.55, 'UP']
        }
        print ("{:<8} {:<15} {:<10} {:<10}".format('Pos','Lang','Percent','Change'))
        for k, v in d.items():
            lang, perc, change = v
            print ("{:<8} {:<15} {:<10} {:<10}".format(k, lang, perc, change))

    case 3:
        dota_teams = ["Liquid", "Virtus.pro", "PSG.LGD", "Team Secret"]
        data = [[1, 2, 1, 'x'],
        ['x', 1, 1, 'x'],
        [1, 'x', 0, 1],
        [2, 0, 2, 1]]
        format_row = "{:>12}" * (len(dota_teams) + 1)
        print(format_row.format("", *dota_teams))
        for team, row in zip(dota_teams, data):
            print(format_row.format(team, *row))

    case 4:
        ## Python program to understand the usage of tabulate function for printing tables in a tabular format
        from tabulate import tabulate
        data = [[1, 'Liquid', 24, 12],
        [2, 'Virtus.pro', 19, 14],
        [3, 'PSG.LGD', 15, 19],
        [4,'Team Secret', 10, 20]]
        print (tabulate(data, headers=["Pos", "Team", "Win", "Lose"]))

    case 5:
        ## Python program to understand, how to print tables using pandas data frame
        import pandas
        data = [[1, 'Liquid', 24, 12],
        [2, 'Virtus.pro', 19, 14],
        [3, 'PSG.LGD', 15, 19],
        [4,'Team Secret', 10, 20]]
        headers=["Pos", "Team", "Win", "Lose"]
        print(pandas.DataFrame(data, headers, headers))
        print('                                         ')
        print('-----------------------------------------')
        print('                                         ')
        print(pandas.DataFrame(data, headers))

    case 6:
        rRed =      ['RED',     'RED',  'RD', 'RE']
        rBlue    =  ['BLUE',    'BLU',  'BL', 'BL']
        rYellow =   ['YELLOW',  'YLO',  'YL', 'YE']
        rGreen =    ['GREEN',   'GRN',  'GR', 'GN']
        rOrange =   ['ORANGE',  'ORG',  'OR', 'OG']
        rPurple =   ['PURPLE',  'PPL',  'PL', 'PR']
        rCyan =     ['CYAN',    'CYN',  'CY', 'CN']
        rBrown =    ['BROWN',   'BRN',  'BR', 'BN']
        rWhite =    ['WHITE',   'WHT',  'WT', 'WH']
        rPink =     ['PINK',    'PNK',  'PK', 'PN']
        rFull_Colour_List = [rRed,rBlue,rYellow,rGreen,rOrange,rPurple,rCyan,rBrown,rWhite,rPink]

    case 7:
        list_cards = []

        test_table = 1


        rRed =      ['RED',     'RED',  'RD', 'RE']
        rBlue    =  ['BLUE',    'BLU',  'BL', 'BL']
        rYellow =   ['YELLOW',  'YLO',  'YL', 'YE']
        rGreen =    ['GREEN',   'GRN',  'GR', 'GN']
        rOrange =   ['ORANGE',  'ORG',  'OR', 'OG']
        rPurple =   ['PURPLE',  'PPL',  'PL', 'PR']
        rCyan =     ['CYAN',    'CYN',  'CY', 'CN']
        rBrown =    ['BROWN',   'BRN',  'BR', 'BN']
        rWhite =    ['WHITE',   'WHT',  'WT', 'WH']
        rPink =     ['PINK',    'PNK',  'PK', 'PN']
        resp = [rRed,rBlue,rYellow,rGreen,rOrange,rPurple,rCyan,rBrown,rWhite,rPink]

        grid = ( "\n" +
            ' {:13} │ {:07} │ {:07} │  \n'
            '───────────────────────────────────────────────────────\n'
            ' {:13} │ {:07} │ {:07} │  \n'
            ' {:13} │ {:07} │ {:07} │  \n'
            ' {:13} │ {:07} │ {:07} │  \n'
            ' {:13} │ {:07} │ {:07} │  \n'
            ' {:13} │ {:07} │ {:07} │  \n'
            ' {:13} │ {:07} │ {:07} │  \n'
            ' {:13} │ {:07} │ {:07} │  \n'

        ).format(
            #   PEG ONE                     PEG TWO                   PEG THREE 
            format(resp[0][0], ' <6'), format(resp[0][1], ' <6'), format(resp[0][2], ' <6'),
            format(resp[1][0], ' <6'), format(resp[1][1], ' <6'), format(resp[1][2], ' <6'),                           
            format(resp[2][0], ' <6'), format(resp[2][1], ' <6'), format(resp[2][2], ' <6'),             
            format(resp[3][0], ' <6'), format(resp[3][1], ' <6'), format(resp[3][2], ' <6'),
            format(resp[4][0], ' <6'), format(resp[4][1], ' <6'), format(resp[4][2], ' <6'),
            format(resp[5][0], ' <6'), format(resp[5][1], ' <6'), format(resp[5][2], ' <6'),
            format(resp[6][0], ' <6'), format(resp[6][1], ' <6'), format(resp[6][2], ' <6'),
            format(resp[7][0], ' <6'), format(resp[7][1], ' <6'), format(resp[7][2], ' <6'),
        )

        print(grid)

    case 8:
        lst = [1, 2, 3]
        print('\n'.join('{}: {}'.format(*k) for k in enumerate(lst)))

    case 9:
        Instrument_list = ['Triangle', 'Whistle', 'Piano', 'Kazoo', 'Harp']
        test = ("hello {} my name is {} {} {} {} ".format(*Instrument_list))
        print(test)


    case 10:
        hrts = ['A♡', '2♡', '3♡', '4♡', '5♡', '6♡', '7♡', '8♡', '9♡', '10♡', 'J♡', 'Q♡', 'K♡']
        dmds = ['A♢', '2♢', '3♢', '4♢', '5♢', '6♢', '7♢', '8♢', '9♢', '10♢', 'J♢', 'Q♢', 'K♢']
        clbs = ['A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']
        spds = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠']

        table2 = (
            '\n'
            '          │ A  │ 2  │ 3  │ 4  │ 5  │ 6  │ 7  │ 8  │ 9  │ 10 │ J  │ Q  │ K  │\n'
            '──────────│────│────│────│────│────│────│────│────│────│────│────│────│────│\n'
            ' Hearts   │ {0} │ {0} │ {0} │ {0} │ {0} │ {0} │ {0} │ {0} │ {0} │ {0} │ {0} │ {0} │ {0} │\n'
            ' Diamonds │ {1} │ {1} │ {1} │ {1} │ {1} │ {1} │ {1} │ {1} │ {1} │ {1} │ {1} │ {1} │ {1} │\n'
            '\n'
        ).format(
            format(*k) for k in enumerate(hrts))

        
        print(table2)

    case 11:


        hrts = ['A♡', '2♡', '3♡', '4♡', '5♡', '6♡', '7♡', '8♡', '9♡', '10♡', 'J♡', 'Q♡', 'K♡']
        dmds = ['A♢', '2♢', '3♢', '4♢', '5♢', '6♢', '7♢', '8♢', '9♢', '10♢', 'J♢', 'Q♢', 'K♢']
        clbs = ['A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']
        spds = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠']
        
        table2 = (
            '\n'
            '          │ A  │ 2  │ 3  │ 4  │ 5  │ 6  │ 7  │ 8  │ 9  │ 10   │ J  │ Q  │ K  │\n'
            '──────────│────│────│────│────│────│────│────│────│────│──────│────│────│────│\n'
            ' Hearts   │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {:3} │ {} │ {} │ {} │\n'
            ' Diamonds │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {:3} │ {} │ {} │ {} │\n'
        ).format(*hrts, *dmds)

        print(table2)


    case 12:
        suit_clubs      = ['2Cl', '3Cl', '4Cl', '5Cl', '6Cl', '7Cl', '8Cl', '9Cl', '0Cl', 'JCl', 'QCl', 'KCl', 'ACl']
        suit_spades     = ['2Sp', '3Sp', '4Sp', '5Sp', '6Sp', '7Sp', '8Sp', '9Sp', '0Sp', 'JSp', 'QSp', 'KSp', 'ASp']
        suit_diamonds   = ['2Di', '3Di', '4Di', '5Di', '6Di', '7Di', '8Di', '9Di', '0Di', 'JDi', 'QDi', 'KDi', 'ADi']
        suit_hearts     = ['2He', '3He', '4He', '5He', '6He', '7He', '8He', '9He', '0He', 'JHe', 'QHe', 'KHe', 'AHe']
        all_suits = [suit_clubs, suit_spades, suit_diamonds, suit_hearts]


        hrts = ['A♡', '2♡', '3♡', '4♡', '5♡', '6♡', '7♡', '8♡', '9♡', '10♡', 'J♡', 'Q♡', 'K♡']
        dmds = ['A♢', '2♢', '3♢', '4♢', '5♢', '6♢', '7♢', '8♢', '9♢', '10♢', 'J♢', 'Q♢', 'K♢']
        clbs = ['A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣']
        spds = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠']
        all_cards = [hrts, dmds, clbs, spds]

        # current goal
        # make a table of 4 columns, 13 rows. Enter an X or an O if the card exists

        table =  (
            '\n'
            '┌──────────────────────────────────────────────────────┐\n'
            '│{}                                                    │\n'
            '│                                                      │\n'
            '│                                                      │\n'
            '│    {}                                                │\n'
            '│                                                      │\n'
            '│                                                      │\n'
            '│       {}                                             │\n'
            '└──────────────────────────────────────────────────────┘'
        )

        table2 = (
            '\n'
            '          │ A  │ 2  │ 3  │ 4  │ 5  │ 6  │ 7  │ 8  │ 9  │ 10   │ J  │ Q  │ K  │\n'
            '──────────│────│────│────│────│────│────│────│────│────│──────│────│────│────│\n'
            ' Hearts   │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {:4} │ {} │ {} │ {} │\n'
            ' Diamonds │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {:4} │ {} │ {} │ {} │\n'
            ' Clubs    │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {:4} │ {} │ {} │ {} │\n'
            ' Spades   │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {} │ {:4} │ {} │ {} │ {} │\n'
            '\n'
        ).format(format(*hrts, ' <2'))
        
        #format(*hrts, *dmds, *clbs, *spds).format(*hrts)
        print(table2)

