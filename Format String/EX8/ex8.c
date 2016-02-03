#include <stdio.h>
int main(int argc, char *argv[]){
int i = 1111;
printf("i value before writing : %d \n",i );
printf("12345%n", &i);
printf("\n i value after writing : %d \n", i);
printf(argv[1]);
return 0;
}
