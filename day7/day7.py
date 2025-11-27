import time
import dask
from dask import delayed, compute
import random


def runAgentSimulation(agentId):
    """
    Simulates an agent doing work (thiking, querying db etc.)
    This takes a random amount of time
    """
    sleepTime = random.uniform(0.5, 1.5)
    time.sleep(sleepTime)

    return {
        "id": agentId,
        "status": "Success",
        "duration": round(sleepTime, 2)
    }


def main():

    totalAgents = 100
    print(f"Starting simulation for {totalAgents} agents")

    # the slow way (serial)
    # result = [runAgentSimulation(i) for i in range(totalAgents)]

    # the fast way (parallel with dask)
    startTime = time.time()

    lazyResults = []
    # wrap the function call in dusk delayed
    # this doesn't run the function yet, it just plans it 
    for i in range(totalAgents):
        task = delayed(runAgentSimulation)(i)
        lazyResults.append(task)

    print("Tasks scheduled. computing now...")
    # dask.compute() triggers the parallel execution
    # it figures out number of cores and distributes the work
    results = compute(*lazyResults)

    endTime = time.time()

    print("Simulation complete")
    print(f"Total time taken: {(endTime-startTime):.2f} seconds")

    serialTime = sum(r['duration'] for r in results)

    print(f"Time if run serially: {serialTime:.2f} seconds")

    print(f"Speedup: {serialTime/(endTime-startTime):.1f}x")

    for res in results[:3]:
        print(res)


if __name__ == "__main__":
    main()
    
    
    
