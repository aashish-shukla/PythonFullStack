from sys import argv
from src import service
def main():
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    with open(file_path ,  "r") as file  :
        for line in file  :
            arr =   line.split()
            if arr[0] == "BALANCE" :
                service.balance(arr[1] , arr[2])
            if arr[0] == "CHECK_IN" :
                service.check_in(arr[1] , arr[2] , arr[3])
            if arr[0] == "PRINT_SUMMARY" :
                print(service.summary())

    
if __name__ == "__main__":
    main()