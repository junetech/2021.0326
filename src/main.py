import sys
from pathlib import Path

import models

# problem_name = ['Flowshop','Non-Flowshop','Hybridflowshop','Distributedflowshop','Nowaitflowshop','Setupflowshop','Tardinessflowshop','TCTflowshop','Jobshop','Flexiblejobshop','Openshop','Parallelmachine']
# modelType = ['CP','MIP']
# Solver = ['CPLEX','Groubi','Google','Xpress']


try:
    problem_name = sys.argv[1]
    modelType = sys.argv[2]
    computational_time = sys.argv[3]
    First = sys.argv[4]
    Last = sys.argv[5]
except:
    problem_name = "Parallelmachine"
    modelType = "CP"
    computational_time = "10"
    First = "151"
    Last = "151"

try:
    Solver = sys.argv[6]
except:
    Solver = "Google"

try:
    NThreads = int(sys.argv[7])
except:
    NThreads = 4

current_dir = Path()

try:
    address = Path(sys.argv[8])
except:
    address = current_dir.parent / "Instances" / problem_name

try:
    output = Path(sys.argv[9])
except:
    output = current_dir.parent / "Results"
output.mkdir(parents=True, exist_ok=True)


for benchmark in range(int(First), int(Last) + 1):
    if modelType == "CP":
        if Solver not in ["CPLEX", "Google"]:
            continue
        if (
            Solver == "Google"
            and modelType == "CP"
            and problem_name
            not in [
                "Non-Flowshop",
                "Hybridflowshop",
                "Nowaitflowshop",
                "Jobshop",
                "Flexiblejobshop",
                "Openshop",
                "Parallelmachine",
            ]
        ):
            continue
    try:
        n, g, Time, LB, UB, GAP = models.main(
            int(computational_time),
            benchmark,
            problem_name,
            modelType,
            Solver,
            NThreads,
            address,
            output,
        )
        result = open(
            Path(output)
            / "result_{}_{}_{}_{}_{}.txt".format(
                modelType, problem_name, computational_time, NThreads, benchmark
            ),
            "a",
        )
        result.write(
            "\n{}\t {}\t {}\t {}\t {}\t {}\t {}\t {}\t {}\t {}".format(
                problem_name, Solver, modelType, benchmark, n, g, LB, UB, GAP, Time
            )
        )
        result.close()
    except:
        result = open(
            Path(output)
            / "result_{}_{}_{}_{}_{}.txt".format(
                modelType, problem_name, computational_time, NThreads, benchmark
            ),
            "a",
        )
        result.write(
            "\n{}\t {}\t {}\t {}\t {} \t {}".format(
                problem_name,
                Solver,
                modelType,
                benchmark,
                sys.exc_info()[0],
                sys.exc_info()[1],
            )
        )
        result.close()
        print("Error:", sys.exc_info()[0], sys.exc_info()[1])

print("\n\nDone")
