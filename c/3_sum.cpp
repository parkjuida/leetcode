#include <stdio.h>
#include <stdlib.h>

void swap(int* nums, int left, int right) {
	int temp = nums[left];
	nums[left] = nums[right];
	nums[right] = temp;
}

void qsort(int* nums, int pivot, int left, int right) {
	int end = right;
	if (left > right) {
		return;
	}

	while (left < right) {
		if (nums[left] > nums[right]) {
			swap(nums, left, right);
		}
			left++;
			right--;	
	}
	swap(nums, pivot, right);
	qsort(nums, pivot, pivot + 1, right - 1);
	qsort(nums, left, left, end);
}

int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
	qsort(nums, 0, 1, numsSize - 1);
	int maxCandidate = numsSize * (numsSize - 1) / 2;
	int** returnArray = (int**)malloc(sizeof(int*) * 3000);
	return returnArray;
}

int main(void) {
	int nums1[3000];

	int nums[5] = { 5, 4, 3, 2, 1 };
	threeSum(nums, 5, 0, 0);
}
