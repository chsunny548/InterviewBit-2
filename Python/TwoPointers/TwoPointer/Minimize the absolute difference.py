"""
Given three sorted arrays A, B and C of not necessarily same sizes.

Calculate the minimum absolute difference between the maximum and minimum number from the triplet a, b, c such that
a, b, c belongs arrays A, B, C respectively.
i.e. minimize | max(a,b,c) - min(a,b,c) |.

Example :

Input:

A : [ 1, 4, 5, 8, 10 ]
B : [ 6, 9, 15 ]
C : [ 2, 3, 6, 6 ]
Output:

1
Explanation: We get the minimum difference for a=5, b=6, c=6 as | max(a,b,c) - min(a,b,c) | = |6-5| = 1.
"""


class Solution:
    def min_abs_diff(self, a, b, c):
        m, n, p = len(a), len(b), len(c)

        i, j, k = 0, 0, 0
        abs_min = 10000000000
        curr_min = -1

        while i < m and j < n and k < p:
            curr_min = abs(max(a[i], b[j], c[k]) - min(a[i], b[j], c[k]))
            if curr_min < abs_min:
                abs_min = curr_min
            if abs_min == 0:
                break

            if a[i] == min(a[i], b[j], c[k]):
                i += 1
            elif b[j] == min(a[i], b[j], c[k]):
                j += 1
            else:
                k += 1

        return abs_min


s = Solution()
a = [36, 58, 64, 76, 111, 131, 131, 132, 166, 174, 192, 223, 235, 243, 248, 296, 325, 335, 372, 389, 426, 446, 448, 472,
     506, 508, 550, 585, 614, 628, 665, 672, 720, 744, 765, 799, 822, 853, 897, 932, 950, 964, 992, 1025, 1049, 1093,
     1114, 1140, 1148, 1174, 1209, 1255, 1273, 1275, 1285, 1293, 1340, 1361, 1401, 1440, 1474, 1489, 1501, 1522, 1549,
     1550, 1555, 1564, 1605, 1640, 1645, 1666, 1668, 1688, 1702, 1722, 1732, 1776, 1799, 1806, 1810, 1813, 1831, 1866]
b = [-373, -334, -322, -299, -267, -237, -190, -175, -153, -122, -118, -79, -55, -37, -20, -19, 20, 32, 40, 67, 116,
     129, 132, 137, 176, 198, 214, 230, 271, 314, 341, 353, 379, 381, 386, 397, 402, 408, 426, 429, 431, 432, 452, 500,
     543, 590, 597, 631, 660, 668, 684, 722, 762, 778, 826, 831, 834, 841, 888, 898, 940, 956, 996, 998, 1047, 1064,
     1084, 1096, 1121, 1159, 1176, 1178, 1191, 1239, 1283, 1305, 1347, 1353, 1401, 1416, 1459, 1469, 1504, 1517, 1548,
     1574, 1598, 1619, 1623, 1627, 1675, 1681, 1710, 1723, 1731, 1737, 1779, 1823, 1825, 1832, 1834, 1860, 1873, 1881,
     1888, 1923, 1938, 1957, 2000, 2042, 2081, 2090, 2133, 2135, 2145, 2187, 2205, 2226, 2272, 2315, 2349, 2382, 2397,
     2431, 2457]
c = [24, 31, 49, 59, 90, 120, 129, 157, 205, 242, 287, 311, 355, 402, 413, 413, 427, 461, 486, 493, 520, 529, 553, 560,
     596, 620, 631, 654, 674, 705, 705, 706, 751, 790, 837, 872, 918, 965, 987, 996, 1039, 1045, 1079, 1109, 1136, 1179,
     1183, 1232, 1256, 1283, 1316, 1346]

print(s.min_abs_diff(a, b, c))
