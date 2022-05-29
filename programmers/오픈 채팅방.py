def solution(record):
    answer = []
    _command = []
    _id = []
    _name = []
    print(len(record))
    a = len(record)
    for i in range(0, a):
        print(record[i])
        _command, _id, _name = record[i].split()
        #print(_command,_id,_name)

    if _command == "Enter":
        print(f"{_name}님이 들어왔습니다.")


    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))