# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sergio-alejandro <sergio-alejandro@stud    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/13 03:37:55 by sergio-alej       #+#    #+#              #
#    Updated: 2025/12/13 03:39:35 by sergio-alej      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    day_1=int(input("Day 1 harvest: "))
    day_2=int(input("Day 2 harvest: "))    
    day_3=int(input("Day 3 harvest: "))
    total=print(f"Total harvest {day_1+day_2+day_3}")
