def where(n: int) -> list:
    iteration = 1
    coord = [0, 0]
    direction = "up"
    move_record = [0, 0]
    counter = 0
    if n == 1:
        return(coord)

    while iteration < n:
        if direction == "right":
            coord[0] += 1
            counter += 1
            if counter == move_record[0] + 1:
                move_record[0], counter = counter, 0
                direction = "down"
        elif direction == "up":
            coord[1] += 1
            counter += 1
            if counter == move_record[1] + 1:
                move_record[1], counter = counter, 0
                direction = "right"
        elif direction == "down":
            coord[1] -= 1
            counter += 1
            if counter == move_record[1] + 1:
                move_record[1], counter = counter, 0
                direction = "left"
        elif direction == "left":
            coord[0] -= 1
            counter += 1
            if counter == move_record[0] + 1:
                move_record[0], counter = counter, 0
                direction = "up"
        iteration += 1
    return coord


def run():
    try:
        n = int(input("Enter the number in the spiral: "))
    except:
        print("You can only enter an integer.")
    else:
        print(f"The coordinates of {n} are: {where(n)}")



if __name__ == "__main__":
    run()
