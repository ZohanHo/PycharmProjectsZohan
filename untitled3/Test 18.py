nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums  # Оставляет только те что повторяются
nums = filter(lambda x: x > 1, nums) #так как 1 не больше одного. а 2 и 3 больше. длина листа 2
print(len(list(nums)))

