#!/usr/bin/env python
# coding: utf-8

# In[374]:


social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                "last_name":"Olpoc",
                "following":[
                ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                "last_name":"Gonzales",
                "following":[
                    "@chums","@jobenilagan"
                ]
    },
    "@chums" : {"first_name":"Matthew",
            "last_name":"Uy",
            "following":[
                "@bongolpoc","@miketan","@rudyang","@joeilagan"
            ]
    },
    "@jobenilagan":{"first_name":"Joben",
                "last_name":"Ilagan",
                "following":[
                "@eeebeee","@joeilagan","@chums","@joaquin"
                ]
    },
    "@joeilagan":{"first_name":"Joe",
                "last_name":"Ilagan",
                "following":[
                "@eeebeee","@jobenilagan","@chums"
                ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                "last_name":"Ilagan",
                "following":[
                "@jobenilagan","@joeilagan"
                ]
    },
    }

def relationship_status(from_member, to_member, social_graph):

    #TRUE OR FALSE: does from_member follow to_member?
    from_member_follow_to_member = to_member in social_graph.get(from_member, {}).get("following", [])
    #TRUE OR FALSE: does to_member follow from_member?
    to_member_follow_from_member = from_member in social_graph.get(to_member, {}).get("following", [])

    if from_member_follow_to_member & to_member_follow_from_member:
        status = "friends"
    
    elif from_member_follow_to_member:
        status = "follower"

    elif to_member_follow_from_member:
        status = "followed by"

    else:
        status = "no relationship"

    return status 

relationship_status("@eeebeee", "@joeilagan", social_graph)


# In[376]:


board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]
    
def tic_tac_toe(board):
    size_of_board = len(board)
    board_string_row = ""
    board_string_column = ""
    diagonal_one = ""
    diagonal_two = ""

    # Check rows
    for i in range(size_of_board):
        # Reset per row
        board_string_row = ""
        for j in range(size_of_board):
            board_string_row += board[i][j]
        if "X" * size_of_board in board_string_row:
            return "X"
        elif "O" * size_of_board in board_string_row:
            return "O"
    
    # Check columns
    for i in range(size_of_board):
        # Reset per column
        board_string_column = ""
        for j in range(size_of_board):
            board_string_column += board[j][i]
        if "X" * size_of_board in board_string_column:
            return "X"
        elif "O" * size_of_board in board_string_column:
            return "O"
    
    # Check diagonals
    for i in range(size_of_board):
        diagonal_one += board[i][i]
        diagonal_two += board[i][size_of_board - 1 - i]
    
    if diagonal_one == "X" * size_of_board:
        return "X"
    elif diagonal_one == "O" * size_of_board:
        return "O"
    
    if diagonal_two == "X" * size_of_board:
        return "X"
    elif diagonal_two == "O" * size_of_board:
        return "O"
    
    return "NO WINNER"

tic_tac_toe(board6)


# In[378]:


legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

def eta(first_stop, second_stop, route_map):

    travel_time = 0

    while first_stop != second_stop:
        for (start, end), leg_info in route_map.items():
            if start == first_stop:
                travel_time += leg_info['travel_time_mins']
                first_stop = end
                break

    return (travel_time)

eta ("upd", "dlsu", legs) 

