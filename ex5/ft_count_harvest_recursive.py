# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sergio-alejandro <sergio-alejandro@stud    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/24 20:25:54 by sergio-alej       #+#    #+#              #
#    Updated: 2025/12/24 20:25:56 by sergio-alej      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    until_day = int(input("Days until harvest: "))

    def helper(day):
        if day > until_day:
            print("Haverst time!")
            return
        print(f"Day {day}")
        helper(day + 1)

    helper(1)
