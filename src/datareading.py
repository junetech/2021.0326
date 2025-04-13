from typing import TextIO


class struct:
    """Structure for instance data"""

    def __init__(self):
        self.n = 0  # jobs
        self.g = 0  # stages
        self.f = 0  # factories

        self.o = []  # operations
        self.p = []  # processing_times
        self.r = []  # routes
        self.m = []  # machine
        self.d = []  # duedates
        self.s = []  # setup


def read_ints(data: TextIO) -> list[int]:
    """Reads a line from a file-like object and returns a list of integers.

    This function reads a single line from the provided text stream,
    strips leading and trailing whitespace, splits the line into
    whitespace-separated tokens, and converts each token into an integer.

    Args:
        data (TextIO): A file-like object with a readline() method,
                              such as an open file in text mode.

    Returns:
        list[int]: A list of integers parsed from the line.

    Example:
        # Given a file containing the line "3 5 8\n"
        nums = read_ints(file)
        # nums will be [3, 5, 8]
    """
    return [int(x) for x in data.readline().strip().split()]


def dataentry(filename, problemType: str) -> struct:
    """data entry

    Args:
        filename
        problemType (str)

    Returns:
        struct: instance
    """
    instance = struct()
    with open(filename, "r") as data:
        instance.n = int(data.readline().strip().split()[0])
        instance.g = int(data.readline().strip().split()[0])

        if problemType == "Flexiblejobshop":
            instance.o = read_ints(data)
            instance.p = [[] for j in range(instance.n)]
            for j in range(instance.n):
                instance.p[j] = [[] for k in range(instance.o[j])]
                for k in range(instance.o[j]):
                    x = read_ints(data)
                    for i in range(instance.g):
                        instance.p[j][k].append(x[i])
        else:
            # 공통 처리: Flexiblejobshop를 제외한 problemType에 해당
            # 'Flowshop','Non-Flowshop','Hybridflowshop','Distributedflowshop',
            # 'Nowaitflowshop','Setupflowshop','Tardinessflowshop','TCTflowshop',
            # 'Jobshop','Openshop','Parallelmachine'
            instance.p = [read_ints(data)]
            for j in range(instance.n - 1):
                instance.p.append(read_ints(data))

            # 추가적인 특성에 따른 세부 처리
            match problemType:
                case "Distributedflowshop":
                    instance.f = int(data.readline().strip().split()[0])

                case "Hybridflowshop":
                    instance.m = read_ints(data)

                case "Tardinessflowshop":
                    instance.d = read_ints(data)

                case "Setupflowshop":
                    for i in range(instance.g):
                        instance.s.append([])
                        instance.s[i] = [read_ints(data)]
                        for j in range(instance.n - 1):
                            instance.s[i].append(read_ints(data))

                case "Jobshop":
                    instance.r = [read_ints(data)]
                    for j in range(instance.n - 1):
                        instance.r.append(read_ints(data))

    print(instance.n)
    print(instance.g)
    # print(instance.p)
    # if problemType == 'Jobshop':
    #    print(instance.r)

    return instance
