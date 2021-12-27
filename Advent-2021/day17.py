xmin, xmax = 96, 125
ymin, ymax = -144, -98


def min_velocity(target):
    i, p = 0, 0
    while True:
        i += 1
        p += i
        if p >= target:
            #print(i)
            return i


def reach_target(vx, vy):
    x, y = 0, 0
    while x <= xmax and y >= ymin:
        x += vx
        y += vy
        if xmin <= x <= xmax and ymin <= y <= ymax:
            return True
        vy -= 1
        if vx > 0:
            vx -= 1
    return False


def main():
    traj_count = 0
    for vx in range(min_velocity(xmin), xmax + 1):
        for vy in range(ymin, abs(ymin)):
            if reach_target(vx, vy):
                traj_count += 1
    print(traj_count)


if __name__ == "__main__":
    main()
