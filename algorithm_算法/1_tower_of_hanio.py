"""
三个柱子A，B，C；A上有着若干大小不一的圆盘，并按从小到大从上至下依次排列。
每次移动一块圆盘，小的必须放置于大的上面，试问需要如何移动让A上所有圆盘完整移动到其他柱子上
"""

'''
思路：
    由于整塔需要移动，小的必须大的之上，得，底盘必须移动且除底盘外塔需完整转移到另一柱子上，得，若需解决N层塔问题，
    先解决N-1层塔问题，得，先解决一层塔问题
    
'''
# num = int(input('输入圆盘个数'))


def hstartnio(start, temp, target, n):
    # 设定终止条件，也为最基本问题
    if n == 1:
        print(f'{start}->{target}')
    else:
        hstartnio(start, target, temp, n - 1)
        print(f'{start}->{target}')
        hstartnio(temp, start, target, n - 1)


hstartnio('A', 'B', 'C', 500)
