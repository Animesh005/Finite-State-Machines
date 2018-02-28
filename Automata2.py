import itertools


def intersect(a, b):
    return list(set(a) & set(b))


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


def convert_str(temp):
    z = ''
    for i in range(len(temp)):
        z = z + temp[i]
    return z


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


states_number = int(input("Enter the number of states : "))

states_out_list = [[0 for x in range(2)] for y in range(states_number)]
states_next_list = [[0 for x in range(2)] for y in range(states_number)]
linked_list = [[0 for x in range(3)] for y in range(states_number)]

states = list(input("Enter the states : "))

for k in range(states_number):
    print("The ", k + 1, " row : ")
    temp = list(input("Enter : "))

    for l in range(len(temp)):
        states_out_list[k][l] = temp[l]

for k in range(states_number):
    print("The ", k + 1, " row : ")
    temp = list(input("Enter : "))

    for l in range(len(temp)):
        states_next_list[k][l] = temp[l]
p1x0 = []
p1x1 = []

for k in range(states_number):
    if int(states_out_list[k][0]) == 0:
        p1x0.append(states[k])
    else:
        p1x1.append(states[k])

if not len(p1x0) == 0 or len(p1x1) == 0:
    p1x0 = []
    p1x1 = []
    for k in range(states_number):
        if int(states_out_list[k][1]) == 0:
            p1x0.append(states[k])
        else:
            p1x1.append(states[k])

P = [convert_str(p1x0), convert_str(p1x1)]
print(P)

for k in range(states_number):
    linked_list[k][0] = states[k]
    linked_list[k][1] = states_out_list[k][0]
    linked_list[k][2] = states_out_list[k][1]


def output_binary(ist, bs):
    bl = list(bs)
    var1 = 2

    for i in range(len(bl) - 1):
        if bl[i] == '0':
            for j in range(states_number):
                if ist == states[j]:
                    ist = states_next_list[j][0]
                    break
        else:
            for j in range(states_number):
                if ist == states[j]:
                    ist = states_next_list[j][1]
                    break
    if bl[-1] == '0':
        for m in range(states_number):
            if ist == states[m]:
                var1 = states_out_list[m][0]
                break
    else:
        for m in range(states_number):
            if ist == states[m]:
                var1 = states_out_list[m][1]
                break

    return var1


Px = []
count = 9
for n in P:
    p1x0 = []
    p1x1 = []
    k = list(n)
    var2 = ["".join(i) for i in itertools.product("01", repeat=count)]
    for j in range(len(var2)):
        output = []
        p1x0 = []
        p1x1 = []
        for l in k:
            output.append(output_binary(l, var2[j]))
        for s in range(len(output)):
            if int(output[s]) == 0:
                p1x0.append(k[s])
            else:
                p1x1.append(k[s])
        if len(p1x0) == 0 or len(p1x1) == 0:
            continue
        else:
            Px.append(convert_str(p1x0))
            Px.append(convert_str(p1x1))

Px = reduce_list_n(Px)
Px.sort(key=len)

i = 0
var2 = ''
while len(var2) != states_number:
    var2 += Px[i]
    i += 1

Px = Px[:i]
print("final state : ", Px)

