winning_numbers_string = input()
winning_numbers_list = list(winning_numbers_string.split(' '))
winning_numbers = [int(num) for num in winning_numbers_list[:-1]]
winning_powerball = int(winning_numbers_list[-1])

num_tickets = int(input())

for i in range(num_tickets):
    all_nums = input()
    all_nums_list = list(all_nums.split(' '))
    main_nums = [int(num) for num in all_nums_list[:-1]]
    powerball = int(all_nums_list[-1])

    count = 0
    match_powerball = False

    for num in main_nums:
        if num in winning_numbers:
            count += 1

    if powerball == winning_powerball:
        match_powerball = True

    print(f'{i + 1}: {count} right, powerball({match_powerball})')