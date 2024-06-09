import DataFromSQL_DB

def milliSecToMin(i:int) -> [int,int]:
    seconds = i // 1000 # Milliseconds to seconds
    minutes = seconds // 60 # Seconds to Minutes
    remainingSeconds = seconds % 60
    return [minutes, remainingSeconds]

def main() -> None:
    timeInMs:List[int] = []

    for i in range(0, len(DataFromSQL_DB.values)):
        timeInMs.append(DataFromSQL_DB.values[i][6])  # 6 index is played 

    # Conversion of Ms to Sec and Min
    formattedTime:List[int,int] = []
    for time in timeInMs:
        formattedTime.append(milliSecToMin(time))

    totalTimeMinutes:int = 0
    totalTimeSeconds:int = 0
    
    for j in formattedTime:
        totalTimeMinutes += j[0]
        totalTimeSeconds += j[1]

    # Adding the remaining seconds to minutes
    totalTimeMinutes += totalTimeSeconds // 60

    print(f"{totalTimeMinutes // 60} hours and {totalTimeMinutes % 60} minutes played")

if __name__ == '__main__':
    main()

else:
    print("This file is meant to run as a script")