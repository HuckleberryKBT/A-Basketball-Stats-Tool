from statistics import mean
from operator import itemgetter
from constants import TEAMS, PLAYERS

#clean player data
def clean_data(players):
    player_list = []
    for player in players:
        dict = {
            'name': player['name'] ,
            'height': int(player['height'].split(' ')[0]),
            'experience': True if player['experience'].upper() == 'YES' else False,
            'guardians': player['guardians'].split(' and ')
        }
        player_list.append(dict)
    return player_list



#Draft players to a team and balance the teams with equal experienced and inexperienced players
def balance_teams(players, teams):
    teams_list = []
    players_per_team = int(len(players)/len(teams))
    # #Create a Dictionary for each team and append it to a Teams list
    ##Save experienced, inexperienced, and avg_height in the teams data structure
    for team in teams:
        teams_list.append({'name': team, 'players': [], 'experienced': 0, 'inexperienced': 0, 'avg_height': 0})
    drafted_players = []
    for team in teams_list:
        for player in players:
            if player in drafted_players:
                continue
            else:
                if player['experience'] == True and team['experienced'] < 3 and len(team) < players_per_team:
                    team['players'].append(player)
                    team['experienced'] += 1
                    team['avg_height'] = avg_height(team)
                    drafted_players.append(player)
                elif player['experience'] == False and team['inexperienced'] < 3 and len(team) < players_per_team:
                    team['players'].append(player)
                    team['inexperienced'] += 1
                    team['avg_height'] = avg_height(team)
                    drafted_players.append(player)
    return teams_list
        
    
#display main greeting
def display_greeting(greeting):
    print('*' * 60)
    print(f'\n{greeting}\n')
    print('*' * 60)


#display main menu options
def display_main_menu():
    print("\nPlease select an option:")
    print("\n1) Display Team Stats")
    print("2) QUIKPICK -  Our patented AI technology predicts who will win the championship.")
    print("3) Quit\n")
    try:
        option = int(input("Enter an option: "))
        if option < 1 or option > 3:
            raise ValueError('\n *-*-*-*- Please enter a valid option: [1  2  3] -*-*-*-*')
    except ValueError:
        print('\n *-*-*-*- Please enter a valid option: [1  2  3] -*-*-*-*')
    else:        
        return option


#Join guardian lists and convert to string
def player_guardians_to_string(team):
    player_guardians_list = []
    for player in team['players']:
        player_guardians_list += player['guardians']
    player_guardians_string = ', '.join(player_guardians_list)
    return player_guardians_string



#Sort players by height and convert player list to a string
def player_roster_to_string(team):
    sorted_by_height = sorted(team['players'], key=itemgetter('height'), reverse=True) 
    player_names = [player['name'] for player in sorted_by_height]
    roster_string = ', '.join(player_names)
    return roster_string

#calculate average player height
def avg_height(team):
    heights_of_players = []
    for player in team['players']:
        heights_of_players.append(player['height'])
    return round(mean(heights_of_players),2)


#quikpik 
def quikpik():
    our_pick = "\nUNBELIEVEABLE! It looks like all teams are perfectly balanced so we can't make a recommendation! Flip a coin - good luck! We hope you win big!\n"
    print()
    print("*" * len(our_pick))
    print(our_pick)
    print("*" * len(our_pick))

#diaplay a goodbye message
def end():
    print("*" * 80)
    print("\nThanks for using BetOnline Sports Betting. Have a great day. Goodbye\n")
    print("*" * 80)


#prompt the user to select a team and display team stats
def display_team_stats(teams):
    while True:
        print('\nWhich team stats would you like to see?\n')
        for i, team in enumerate(teams):
            print(f"{i + 1}) {team['name']}")
        print('0) Go back')
        try:
            option = int(input('\nEnter an option: '))
            if option < 0 or option > len(teams):
                raise ValueError('\n*-*-*-*- Please enter the number corresponding to your team selection. -*-*-*-*')

        except ValueError:
            print('\n*-*-*-*-Please enter the number corresponding to your team selection.*-*-*-*')
        else:
            if option != 0:
                selected_team = teams[option-1]
                roster = player_roster_to_string(selected_team)
                guardians = player_guardians_to_string(selected_team)
                print('-' * 100)
                print(f"\n{'-' * 40} Team: {selected_team['name'].upper()} {'-' * 40}\n")
                print('-' * 100)
                print(f"Total players: {len(selected_team['players'])}")
                print(f"Experienced players:{selected_team['experienced']}")
                print(f"Inexperienced players:{selected_team['inexperienced']}")
                print(f"Average height: {selected_team['avg_height']} inches")
                print(f"\nRoster:\n{'-' * 20}\n{roster}")
                print(f"\nParents/Guardians:\n{'-' * 20}\n{guardians}\n")
                print('-' * 100 + '\n')
                print('*' * 100 + '\n')
                print('-' * 100)
            break   


##Start tool
def start(PLAYERS, TEAMS):
    cleaned_player_data = clean_data(PLAYERS)    
    balanced_teams = balance_teams(cleaned_player_data, TEAMS)
    display_greeting('Welcome to BetOnline Sports Betting')
    while True:
        action = display_main_menu()
        if action ==  1:
            display_team_stats(balanced_teams)
        elif action == 2:
            quikpik()
        elif action == 3:
            end()
            break


if __name__ == '__main__':
    start(PLAYERS, TEAMS)





