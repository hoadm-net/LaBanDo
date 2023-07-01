from os import getcwd, path, mkdir
from .utilities import clean_folder, zip_test_case


class Problem:
    def __init__(self) -> None:
        self.case_index = 1
        self.points = {}
        self.base = getcwd()
        self.name = str(self.__class__.__name__).lower()
        self.output_dir = path.join(self.base, 'outputs', self.name)

        if path.exists(self.output_dir):
            clean_folder(self.output_dir)
        else:
            mkdir(self.output_dir)

    def __create_config_file(self) -> None:
        with open(path.join(self.output_dir, 'init.yml'), 'w+') as writer:
            writer.write(f"archive: {self.name}.zip\n")
            writer.write(f"test_cases:\n")
            for idx in range(1, self.case_index):
                writer\
                    .write(f"- {{in: {self.name}.{idx}.in, out: {self.name}.{idx}.out, points: {self.points[idx]}}}\n")

    def _solve(self, test_data: list[str]) -> str:
        raise NotImplemented(f"solve method must be implemented in subclass!!")

    def __zip_in_out(self) -> None:
        zip_test_case(self.output_dir, self.name)

    def __read_input(self, test_case_index: int) -> list[str]:
        input_test_case_file = path.join(self.output_dir, f"{self.name}.{test_case_index}.in")
        if not path.exists(input_test_case_file):
            raise FileExistsError(f"Input test case file ({input_test_case_file}) is not exists!!!")

        with open(input_test_case_file, 'r') as reader:
            return reader.readlines()

    def __write_output_string(self, data: str, test_case_index: int) -> None:
        with open(path.join(self.output_dir, f"{self.name}.{test_case_index}.out"), 'w+') as writer:
            writer.write(data)

    def add_test_case_from_string(self, test_case: str, point: int) -> None:
        with open(path.join(self.output_dir, f"{self.name}.{self.case_index}.in"), 'w+') as writer:
            writer.write(test_case)
        self.points[self.case_index] = point
        self.case_index += 1

    def add_test_case_from_list(self, test_case: list, point: int) -> None:
        with open(path.join(self.output_dir, f"{self.name}.{self.case_index}.in"), 'w+') as writer:
            for i in test_case:
                writer.write(f"{i}\n")
        self.points[self.case_index] = point
        self.case_index += 1

    def build(self):
        self.__create_config_file()
        for idx in range(1, self.case_index):
            output_str = self._solve(test_data=self.__read_input(test_case_index=idx))
            if len(output_str) == 0:
                raise ValueError('Output data is empty!!!')
            self.__write_output_string(data=output_str, test_case_index=idx)
        self.__zip_in_out()
