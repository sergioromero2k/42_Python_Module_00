# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sergio-alejandro <sergio-alejandro@stud    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/13 03:39:51 by sergio-alej       #+#    #+#              #
#    Updated: 2025/12/13 03:44:18 by sergio-alej      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def ft_plant_age():
    age = int(input("Enter plant age in days:  "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
