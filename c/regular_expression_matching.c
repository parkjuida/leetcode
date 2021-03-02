#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
#include<stdbool.h>
#include<string.h>


typedef struct step {
	int index_s;
	int index_p;
} step;

typedef struct stack_struct {
	step steps[50];
	int stack_index;
} stack_struct;

void stack_add(stack_struct *stack, step item) {
	stack->steps[stack->stack_index++] = item;
}

step stack_pop(stack_struct *stack) {
	return stack->steps[--stack->stack_index];
}

char* remove_duplications(char* s, char *new_p) {
	int j = 0;

	for (int i = 0; i < strlen(s); ++i) {
		if (i + 3 < strlen(s) && s[i] == s[i + 2] && s[i + 1] == '*' && s[i + 3] == '*') {
			i += 1;
		}
		else {
			new_p[j] = s[i];
			j++;
		}
	}
	new_p[j] = '\0';

	return new_p;
}

bool isMatch(char* s, char* p) {
	char new_p[31];
	remove_duplications(p, new_p);

	stack_struct *stack = (stack_struct*)malloc(sizeof(stack_struct));

	stack->stack_index = 0;
	step curr ;
	curr.index_s = 0;
	curr.index_p = 0;

	int len_p = strlen(new_p);
	int len_s = strlen(s);

	stack_add(stack, curr);

	while (stack->stack_index > 0) {
		curr = stack_pop(stack);

		if (curr.index_p == len_p && curr.index_s == len_s)
			return true;
		if (curr.index_p > len_p || curr.index_s > len_s)
			continue;

		if (curr.index_p + 1 < strlen(new_p) && new_p[curr.index_p + 1] == '*') {
			curr.index_p += 2;
			stack_add(stack, curr);
			curr.index_p -= 2;

			if (new_p[curr.index_p] == '.' || s[curr.index_s] == new_p[curr.index_p]) {
				curr.index_s++;
				stack_add(stack, curr);
				curr.index_p += 2;
				stack_add(stack, curr);
			}
		}
		else {
			if (new_p[curr.index_p] == '.' || s[curr.index_s] == new_p[curr.index_p]) {
			curr.index_s++;
			curr.index_p++;
			stack_add(stack, curr);
			}
		}
	}

	return false;
}


int main() {
	char *s = "aa";
	char *p = "a";

	printf("%d", isMatch(s, p));
	
	s = "aa";
	p = "a*";

	printf("%d", isMatch(s, p));

	s = "ab";
	p = ".*";

	printf("%d", isMatch(s, p));

	s = "aab";
	p = "c*a*b";

	printf("%d", isMatch(s, p));

	s = "mississippi";
	p = "mis*is*p*.";

	printf("%d", isMatch(s, p));

	s = "ab";
	p = ".*c";

	printf("%d", isMatch(s, p));

	s = "";
	p = "c*c*";

	printf("%d", isMatch(s, p));

	s = "aaaaaaaaaaaaab";
	p = "a*a*a*a*a*a*a*a*a*a*c";
	
	printf("%d", isMatch(s, p));

	return 0;
}