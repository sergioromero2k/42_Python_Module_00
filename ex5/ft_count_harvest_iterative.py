# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sergio-alejandro <sergio-alejandro@stud    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/24 20:25:47 by sergio-alej       #+#    #+#              #
#    Updated: 2025/12/24 20:25:49 by sergio-alej      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    until_day = int(input("Days until harvest: "))
    for i in range(until_day):
        print(f"Day {i+1}")
    print("Harvest time!")