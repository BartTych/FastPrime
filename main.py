
import datetime
import Prime
import error_check

StaticMethods = Prime.BasicOperations()

# setup

N = 1 * 10 ** 7
start = 5 * 10 ** 10
size = 200

type_of_action = 2
# 0 - search for primes in range (0, N)
# N is limited to ~2*10**9 depending on your ram size

# 1 - Search for primes in range (start_of_search, start_of_search + size)
# (start + size) is limited to N^2, size is limited by your ram size

# 2 - read pickled numbers

display_all_results = 1
# 0 - no
# 1 - yes
# also applicable if read from pickle

display_largest_primes_found = 1
how_many = 20
# 0 - no
# 1 - yes, set up how many , display all is ignored
# also applicable for read from pickle action

store_result_as_pickle = 0
# 0 - no
# 1 - yes
# applicable to action 0 and 1 only

pickle_name = "result"
# used for read or store files

# end of setup


beginning = datetime.datetime.now()


error_check.check_for_input_errors(N, start, size, type_of_action)

if type_of_action == 0:
    A = StaticMethods.calculate_primes_in_range(N)

elif type_of_action == 1:
    A = StaticMethods.calculate_primes_in_range_with_use_base_matrix(N, start, size)

else:
    A = StaticMethods.load_pickle(pickle_name)

end = datetime.datetime.now()
print(f"Calculation time: {end - beginning}")


if type_of_action == 0 and store_result_as_pickle:
    StaticMethods.write_primes_to_pickle(A, "result")

if display_all_results and display_largest_primes_found == 0:
    StaticMethods.disp_primes(A)

if display_largest_primes_found:
    StaticMethods.disp_primes(A, how_many)

if type_of_action != 2 and store_result_as_pickle:
    StaticMethods.write_primes_to_pickle(A, pickle_name)