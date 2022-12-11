import numpy as np
import pickle
import sys


class BasicOperations:

    @staticmethod
    def calculate_primes_in_range(N):
        k = int(np.sqrt(N)) + 1

        A = np.ones(N, bool)
        A[0] = False
        A[1] = False
        divisor = 2
        while divisor < k:
            BasicOperations.__remove_divisor_python(A, divisor, 0)
            print(f"checked divisor of base matrix: {divisor}")
            divisor = BasicOperations.__find_next_divisor_in_bool_matrix(A, divisor)
        A = BasicOperations.__translate_bool_to_int_np(A)

        return A

    @staticmethod
    def calculate_primes_in_range_with_use_base_matrix(N, start, size):
        A = BasicOperations.calculate_primes_in_range(N)
        D = np.mod(start, A)
        B = BasicOperations.__sieve_primes_using_base_matrix(A, start, size, D)

        del A
        del D
        #A = BasicOperations.__translate_bool_to_int_np_with_shift(B, start)
        A = BasicOperations.__translate_bool_to_int_comp_list_with_shift(B,start)
        del B
        return A

    @staticmethod
    def __sieve_primes_using_base_matrix(A, start, number, D):

        k = int((start + number)**0.5) + 1
        divisor = 2
        divisor_index = 0
        B = np.ones(number, bool)
        try:
            while divisor < k:
                BasicOperations.__remove_divisor_with_base_matrix(B, divisor, D, divisor_index)
                print(f"checked divisor of secondary matrix: {BasicOperations.__get_number_as_readable_str(divisor)}")
                divisor, divisor_index = BasicOperations.__find_next_divisor_in_matrix(A, divisor_index)
        except IndexError:
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("remember that start + size is limited by ~ N^2 ")
            sys.exit("execution stopped , N is not large enough")
        return B

    @staticmethod
    def __remove_divisor(A, divisor, start_index):
        index = start_index + 2 * divisor
        while index < len(A):
            A[index] = False
            index += divisor

    @staticmethod
    def __remove_divisor_python(A, divisor, start_index):
        index = start_index + 2 * divisor
        A[index::divisor] = False

    @staticmethod
    def __remove_divisor_with_base_matrix(A, divisor, D, divisor_index):
        rest = D[divisor_index]
        if rest == 0:
            translation = 0
        else:
            translation = int(divisor - rest)
        A[translation::divisor] = False

    @staticmethod
    def __find_next_divisor_in_bool_matrix(A, index):
        for i in range(1, 10*index):
            if A[index + i]:
                return index + i

    @staticmethod
    def __find_next_divisor_in_matrix(A, index):
        return A[index + 1], index + 1

    @staticmethod
    def __translate_bool_to_int(A):
        matrix = []
        for i in range(len(A)):
            if not A[i]:
                matrix.append(i)
        return matrix

    @staticmethod
    def __translate_bool_to_int_comp_list(A):
        matrix = [i for i, n in enumerate(A) if n]
        return matrix

    @staticmethod
    def __translate_bool_to_int_comp_list_with_shift(A,delta):
        matrix = [i + delta for i, n in enumerate(A) if n]
        return matrix

    @staticmethod
    def __translate_bool_to_int_np(A):
        matrix = np.nonzero(A)[0]
        return matrix

    @staticmethod
    def __translate_bool_to_int_np_with_shift(A, delta):
        matrix = np.nonzero(A)[0]
        matrix = matrix + delta
        return matrix

    @staticmethod
    def disp_large_number_as_readable(a):
        print(BasicOperations.__get_number_as_readable_str(a))

    @staticmethod
    def __get_number_as_readable_str(a):
        a = str(a)
        string = ""
        for i, n in enumerate(a):
            # for every third digit add space apart from last one
            if i % 3 == 0 and i < len(a):
                string += ' '
                string += a[-i - 1]  # reversed order
            else:
                string += a[-i - 1]
        return string[::-1]

    @staticmethod
    def load_pickle(file):
        with open(f'{file}.pkl', 'rb') as f:
            x = pickle.load(f)
        return x

    @staticmethod
    def write_primes_to_pickle(data, name):
        with open(f'{name}.pkl', 'wb') as file:
            pickle.dump(data, file)

    @staticmethod
    def disp_primes(primes, number=-1):

        if number == -1:
            print("all primes found:")

            for n in primes:
                BasicOperations.disp_large_number_as_readable(n)
        else:
            print(f"last {number} prime numbers in matrix: ")

            for n in primes[-number:]:
                BasicOperations.disp_large_number_as_readable(n)
