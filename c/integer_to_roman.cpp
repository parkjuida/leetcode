

char* intToRoman(int num) {
	int arr[5] = { 0, 1, 10, 100, 1000 };
	char candidate[8] = { '0', 'I', 'V', 'X', 'L', 'C', 'D', 'M' };
	char answer[13];
	int split, answer_index = 0;

	for (int i = 4; i > 0; --i) {
		while(num / arr[i] == 0) {
			split = num / arr[i];
			num = num - num / arr[i] * arr[i];

			if () {

			}
		}
	}
}

int main(void) {


}