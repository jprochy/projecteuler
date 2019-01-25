import math
def is_pentagonal_number(num):
    n = (0.5 + math.sqrt(0.25 - 6.0 * (-num))) / 3.0
    return n == int(n)


def project_euler_44():
    last_number_1 = 1
    n1 = 2
    best_distance = 1000 * 1000 * 1000

    while True:
        current_number_1 = n1 * (3 * n1 - 1) // 2

        if current_number_1 - last_number_1 > best_distance:
            break

        continue_to_outer_loop = False

        n2 = n1 - 1

        while n2 > 0:
            current_number_2 = n2 * (3 * n2 - 1) // 2

            if current_number_1 - current_number_2 > best_distance:
                continue_to_outer_loop = True
                break

            if is_pentagonal_number(current_number_1 + current_number_2) and is_pentagonal_number(current_number_1 - current_number_2):
                tmp_distance = current_number_1 - current_number_2

                if best_distance > tmp_distance:
                    best_distance = tmp_distance

            n2 -= 1

        n1 += 1

        if continue_to_outer_loop:
            continue

        last_number_1 = current_number_1

    return best_distance

print(project_euler_44())