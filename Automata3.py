import itertools


def convert_str(temp):
    z = ''
    for i in range(len(temp)):
        z = z + temp[i]
    return z


def convert_list(a):
    temp2 = []
    for i in a:
        j = convert_str(list(i))
        temp2.append(j)
    return temp2


def Union(a, b):
    return list(set(a) | set(b))


def intersect(a, b):
    return list(set(a) & set(b))


def difference(a, b):
    return list(set(a) - set(b))


def search_item(index2, item):
    flag = 0
    item = list(item)
    item.sort()
    for i in range(len(index2)):
        z = intersect(list(index2[i]), item)
        z.sort()
        if z == item:
            flag = 1
            break
        else:
            flag = 0
    if flag == 0:
        return False
    else:
        return True


def same_pair(a, b):
    a.sort()
    b.sort()

    if a == b:
        return True
    else:
        return False


def search(index2, item):
    flag = 0
    for i in range(len(index2)):
        if index2[i] == item:
            flag = 1
            break
        else:
            flag = 0
    if flag == 0:
        return False
    else:
        return True


def reduce_list_n(index2):
    temp2 = []
    for i in range(len(index2)):
        if len(temp2) == 0:
            temp2.append(index2[i])

        else:
            if search(temp2, index2[i]) == False:
                temp2.append(index2[i])


    return temp2


states_no = int(input("Enter the number of states : "))
states_list = list(input("Enter the states : "))
print(states_list)
input_no = int(input("Enter the number of inputs : "))

adj_out_list = [[0 for i in range(states_no)] for j in range(states_no)]
adj_state_list = [[0 for i in range(states_no)] for j in range(states_no)]
state_out = [[0 for i in range(input_no)] for j in range(states_no)]
state_next = [[0 for i in range(input_no)] for j in range(states_no)]

for k in range(states_no):
    print("The ", k+1, " row : ")
    temp = list(input("Enter : "))

    for l in range(len(temp)):
        state_out[k][l] = temp[l]
print(state_out)

for k in range(states_no):
    print("The ", k+1, " row : ")
    temp = list(input("Enter : "))

    for l in range(len(temp)):
        state_next[k][l] = temp[l]
print(state_next)

invalid = 0
valid = 1
flag = 0

for k in range(states_no):
    for l in range(states_no):
        if k == l:
            adj_out_list[k][l] = 1

        else:
            for j in range(input_no):
                if state_out[k][j] == '-' or state_out[l][j] == '-':
                    continue
                else:
                    if state_out[k][j] != state_out[l][j]:
                        flag = 0
                        break
                    else:
                        flag = 1
            if flag == 1:
                adj_out_list[k][l] = valid
            else:
                adj_out_list[k][l] = invalid

flag2 = 0

for k in range(states_no):
    for l in range(states_no):
        if k == l:
            adj_out_list[k][l] = valid

        else:
            for j in range(input_no):
                if state_out[k][j] == '-' or state_out[l][j] == '-':
                    flag2 = 0
                    continue
                else:
                    flag2 = 1
                    break

        if flag2 == 0:
            adj_out_list[k][l] = valid


print(adj_out_list)

uninteruppted = 2
interruppted = 3
flag3 = 0

for k in range(states_no):
    for l in range(states_no):
        if k == l:
            adj_state_list[k][l] = uninteruppted

        else:
            for j in range(input_no):
                if state_next[k][j] == '-' or state_next[l][j] == '-':
                    continue
                elif state_out[k][j] == state_out[l][j]:
                    if state_next[k][j] == state_next[l][j]:
                        adj_state_list[k][l] = uninteruppted
                    elif same_pair([states_list[k], states_list[l]], [state_next[k][j], state_next[l][j]]):
                        adj_state_list[k][l] = uninteruppted
                    else:
                        adj_state_list[k][l] = interruppted
                else:
                    adj_state_list[k][l] = invalid

for k in range(states_no):
    for l in range(states_no):
        if k == l:
            adj_state_list[k][l] = uninteruppted

        else:
            for j in range(input_no):
                if state_next[k][j] == '-' or state_next[l][j] == '-':
                    flag3 = 0
                    continue
                else:
                    flag3 = 1
                    break

            if flag3 == 0:
                adj_state_list[k][l] = uninteruppted

flag4 = 1
for k in range(states_no):
    for l in range(states_no):
        if k == l:
            adj_state_list[k][l] = uninteruppted

        else:
            for j in range(input_no):
                if state_out[k][j] == '-' or state_out[l][j] == '-':
                    continue
                else:
                    if state_out[k][j] != state_out[l][j]:
                        flag4 = 0
                        break
                    else:
                        flag4 = 1
            if flag4 == 0:
                adj_state_list[k][l] = invalid

print(adj_state_list)

for k in range(states_no):
    for l in range(states_no):
        var2 = str(states_list[k])+str(states_list[l])
        if list(str(adj_state_list[k][l])) == intersect(list(var2), list(str(adj_state_list[k][l]))):
            adj_state_list[k][l] = uninteruppted

not_compatible_states = []

for k in range(states_no):
    for l in range(states_no):
        if adj_out_list[k][l] == invalid:
            var3 = str(states_list[k])+str(states_list[l])
            not_compatible_states.append(var3)

interruppting_states = [['0' for i in range(states_no)] for j in range(states_no)]
temp2 = []

for k in range(states_no):
    for l in range(states_no):
        if adj_state_list[k][l] == interruppted:
            for j in range(input_no):
                if state_out[k][j] == '-' or state_out[l][j] == '-':
                    continue
                else:
                    var4 = str(state_next[k][j])+str(state_next[l][j])
                    temp2.append(var4)
            interruppting_states[k][l] = temp2
            temp2 = []

print(interruppting_states)

for k in range(len(not_compatible_states)):
    for m in range(states_no):
        for n in range(states_no):
            if search_item(list(interruppting_states[m][n]), not_compatible_states[k]):
                var5 = str(states_list[m])+str(states_list[n])
                not_compatible_states.append(var5)

temp3 = []

for i in range(len(not_compatible_states)):
    z = list(not_compatible_states[i])
    z.sort()
    temp3.append(str(z[0]+str(z[1])))

temp4 = reduce_list_n(temp3)
not_compatible_states = temp4

print("non compatible states : ", not_compatible_states)

templist = []
for i in itertools.combinations(states_list, 2):
    templist.append(list(i))

temp3 = []

for i in range(len(templist)):
    z = list(templist[i])
    z.sort()
    temp3.append(str(z[0]+str(z[1])))

temp4 = reduce_list_n(temp3)
templist = temp4

compatible_states = difference(templist, not_compatible_states)
compatible_states.sort()

print("compatible states : ", compatible_states)

temp_str = convert_str(states_list)
k = len(temp_str)
while k > 1:
    n = temp_str[:k]
    z = list(itertools.combinations(n, 2))
    z = convert_list(z)
    if set(z).issubset(compatible_states):
        break
    k = k - 1

for j in range(len(z)):
    compatible_states.remove(z[j])
compatible_states.append(temp_str[:k])
compatible_states.sort()
print("maximum compatible states : ", compatible_states)


