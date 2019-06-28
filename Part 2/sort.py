file = open("final", "r")
char_list = file.readlines()
final_list = sorted(char_list, key=lambda x: float(x.partition('\', (')[2].rpartition(', ')[0]), reverse = True)
final_list = final_list[0:8000]
out = open("output.txt", "w")
out.writelines(final_list)