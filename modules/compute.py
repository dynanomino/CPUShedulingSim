#This module contains the 
import numpy as np 

def _FCFS(task_info:dict) -> np.ndarray:
    """
    Computes the scheduling base on the first come first serve
    
    Parameters
    ----------

    task_info: dict 
        A dictionary containing both the scheduling algorithm and task details

        The dictionary should contain the following key strings and value types
        presented below:

        {"arrival_time": np.array 1d,
         "wc_exec_time": np.array 1d}

    computed_results: np.array
        A 2d numpy array containing the computed results.

    """

    arrival_time=task_info['arrival_time']
    wx_exec_time=task_info['wc_exec_time']
    task_sorted=np.argsort(arrival_time)
    current_time=0
    computed_results=[]

    for task in task_sorted:
        exec_time=wx_exec_time[task]
        computed_results.append([task,current_time,current_time+exec_time,1])
        current_time+=exec_time    

    computed_results=np.array(computed_results,dtype=float)

    return computed_results

def _rate_monotonic(task_info:dict) -> np.ndarray:
    """
    Computes the scheduling base on the rate monotonic cpu scheduling algorithm

    """
    computed_results=np.array([[]])

    return computed_results    

ALGO_MAPPING={'rate_monotonic':_rate_monotonic,
              'first_come_first_serve':_FCFS}

def cpu_scheduling_compute(task_info: dict) -> np.ndarray:
    """
    Computes the scheduling based on the cpu scheduling algorithm 
    and task details in task_info

    Parameters
    ----------

    task_info: dict 
        A dictionary containing both the scheduling algorithm and task details

        The dictionary and with all the possible the key string and value type 
        is presented below:

        {"sceduling_algo": str,
         "periods": np.array 1d,
         "arrival_time": np.array 1d,
         "wc_exec_time": np.array 1d,
         "invoc_time": np.array 2d,
         "frequency": np.array 1d}
    
    Return 
    --------
    computed_results: np.array
        A 2d numpy array containing the computed results. Each lower dimension 
        contains the following 4 items and their associated type:

        Task_num -> string denoting the task number
        start_time -> float 
        end_time -> float
        frequency -> float 

        An example output is presented below:
        [[Task_num,start_time,end_time,frequency],
         [Task_num,start_time,end_time,frequency],
         ...]
        
    """

    algo=task_info['scheduling_algo']

    computed_results=ALGO_MAPPING[algo](task_info)

    return computed_results