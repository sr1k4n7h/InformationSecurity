#include <stdio.h>
int main(int argc, char *argv[])
{
int value = 0;
printf("value @ %p\n", &value);
printf("before write value = %d\n", value);
if (argc > 1){
printf(argv[1]);
}
putchar('\n');
printf("after write value = %d\n", value);
return 0;
}
