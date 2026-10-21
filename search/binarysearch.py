# Search in Rotated Arrays

"""Tenemos un array de enteros ordenada de forma ascendente sin duplicados
en un indice k la lista esta rotada. Por ejemplo, [0,1,2,4,5,6,7] puede ser rotada en [4,5,6,7,0,1,2].
Nuestro objetivo es encontrar un n[umero, si no lo encotramos, retornamos -1. Debemos hacerlo en O(log n) tiempo.
"""


def RotatedBinarySearch(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(RotatedBinarySearch(nums, target))  # Output: 4

    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    print(RotatedBinarySearch(nums, target))  # Output: -1

    nums = [1]
    target = 0
    print(RotatedBinarySearch(nums, target))  # Output: -1
