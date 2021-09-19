import random
import csv
import matplotlib.pyplot as plt
import numpy as np


def distance(arr1, arr2):
    dimensions = len(arr1)
    sqr_sum = 0
    for i in range(dimensions):
        sqr_sum += (float(arr1[i]) - arr2[i]) ** 2
    return sqr_sum ** 0.5


m = 3
maximum_c = 7
costs = []

with open('data3.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
del data[-1]
dims = len(data[0])

# for row in data:
#     for i in range(maximum_c):
#         row.append(0)


for c in range(3, 4):
    data_cluster = []
    for i in range(len(data)):
        data_cluster.append([0] * c)
    centeroids = []
    for i in range(c):
        tmp = []
        for j in range(dims):
            tmp.append(random.randrange(-10, 600, 1))  # Rangesho dorost kon
        centeroids.append(tmp)

    for rape in range(100):
        for row_num in range(len(data)):
            for i in range(c):
                makhraj = 0
                main_dis = distance(data[row_num], centeroids[i])

                for j in range(c):
                    tmp_dis = distance(data[row_num], centeroids[j])
                    # main_dis = (((float(row[0]) - centeroids[i][0]) ** 2) + (
                    #         (float(row[1]) - centeroids[i][1]) ** 2)) ** 0.5  # Xk -Vi can be done with func
                    # for j in range(c):
                    #     tmp_dis = (((float(row[0]) - centeroids[j][0]) ** 2) + (
                    #             (float(row[1]) - centeroids[j][1]) ** 2)) ** 0.5  # Xk -Vj
                    makhraj += (main_dis / tmp_dis) ** (2 / (m - 1))
                if makhraj == 0:
                    data_cluster[row_num][i] = 1
                else:
                    data_cluster[row_num][i] = 1 / makhraj  # kesafatkari

        for i in range(c):
            soorat_x = 0
            soorat_y = 0
            makhraj_all = 0
            for j in range(len(data)):
                soorat_x += (data_cluster[j][i] ** m) * float(data[j][0])
                soorat_y += (data_cluster[j][i] ** m) * float(data[j][1])
                makhraj_all += (data_cluster[j][i] ** m)
            centeroids[i][0] = soorat_x / makhraj_all
            centeroids[i][1] = soorat_y / makhraj_all

    j = 0
    for k in range(len(data)):
        for i in range(c):
            # j += (((float(row[0]) - centeroids[i][0]) ** 2) + (
            #         (float(row[1]) - centeroids[i][1]) ** 2)) * (row[dims + 2]) ** m
            j += (distance(data[k], centeroids[i]) ** 2) * data_cluster[k][i] ** m
    costs.append(j)
x_axis = [1, 2, 3, 4, 5]
# plt.plot(x_axis, costs)
# plt.show()
crisp_clusters = []
for i in range(len(data)):
    crisp_clusters.append(data_cluster[i].index(max(data_cluster[i])))
# cluster0 = []
# cluster1 = []
# cluster2 = []
#
# for i in range(len(data)):
#     if crisp_clusters[i] == 0:
#         cluster0.append(data[i])
#     elif crisp_clusters[i] == 1:
#         cluster1.append(data[i])
#     elif crisp_clusters[i] == 2:
#         cluster2.append(data[i])
# plt.scatter(cluster0[:, 0], cluster0[:, 1])
# plt.scatter(cluster1[:, 0], cluster1[:, 1], c='r')
# plt.scatter(centeroids[0][:, 0], centeroids[1][:, 1], s=80, c='y', marker='s')
# plt.xlabel('Test Data'), plt.ylabel('Z samples')
# plt.show()

myshitcolor = []
for row_num in range(len(data)):
    tmp = 0
    for i in range(3):
        tmp += data_cluster[row_num][i]
    tmp += 2 * data_cluster[row_num][crisp_clusters[row_num]]
    myshitcolor.append(tmp/5)
print(myshitcolor)


x_cords = []
y_cords = []
for row in data:
    x_cords.append(float(row[0]))
    y_cords.append(float(row[1]))

fig = plt.figure()
ax = fig.add_subplot(111)
colors = ['r', 'g', 'b']
Labels = ['RED', 'GREEN', 'BLUE']
colors = np.asarray(colors)
colorslist = colors[crisp_clusters]
Labels = np.asarray(Labels)
labellist = Labels[crisp_clusters]
for x, y, c, l in zip(x_cords, y_cords, colorslist, labellist):
    ax.scatter(x, y, color=c, label=l)

handles, labels = ax.get_legend_handles_labels()

newLeg = dict()
for h, l in zip(handles, labels):
    if l not in newLeg.keys():
        newLeg[l] = h

handles = []
labels = []
for l in newLeg.keys():
    handles.append(newLeg[l])
    labels.append(l)

ax.legend(handles, labels)
for i in range(3):
    plt.scatter(centeroids[i][0], centeroids[i][1], s=80, c='y', marker='s')
plt.show()
