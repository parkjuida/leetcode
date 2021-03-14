#include <stdio.h>

int max(int a, int b) {
	if (a > b)
		return a;
	else
		return b;
}

int min(int a, int b) {
	if (a < b)
		return a;
	else
		return b;
}

int maxArea(int* height, int heightSize) {
	int left = 0, right = heightSize - 1;
	int area = 0;

	while (left < right) {
		area = max(area, (right - left) * min(height[right], height[left]));

		if (height[right] < height[left]) {
			right--;
		}
		else {
			left++;
		}
	}

	return area;
}

int main(void) {
	int arr[3000] = { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
	printf("%d", maxArea(arr, 9));

}