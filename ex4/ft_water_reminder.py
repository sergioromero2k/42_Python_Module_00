# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: sergio-alejandro <sergio-alejandro@stud    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/24 20:25:41 by sergio-alej       #+#    #+#              #
#    Updated: 2025/12/24 20:25:43 by sergio-alej      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    age = int(input("Days since last watering: "))
    if age > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
