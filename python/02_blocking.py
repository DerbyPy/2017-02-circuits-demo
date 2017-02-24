def task():
    print('Starting task')
    x = 1
    while x < 30000000:
        x += 1

    print('Now we are finally done.')


if __name__ == '__main__':
    task()
    print('Continuing main execution...')
