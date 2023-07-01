from hmd import Problem
from random import randint


class APlusB(Problem):
    def _solve(self, test_data: list[str]) -> str:
        output_str = ''
        n = int(test_data[0])
        for i in range(n):
            line = test_data[i + 1].split()
            a = int(line[0])
            b = int(line[1])
            output_str += f"{a+b}\n"

        return output_str


if __name__ == '__main__':
    problem = APlusB()

    # test case 1
    problem.add_test_case_from_string(test_case="2\n2 2\n5 7", point=50)

    # test case 2
    tc_2_n = 10
    tc_2 = [f"{randint(1, 1000)} {randint(1, 1000)}" for _ in range(tc_2_n)]
    tc_2.insert(0, str(tc_2_n))
    problem.add_test_case_from_list(test_case=tc_2, point=50)

    # build
    problem.build()
