#include <stdio.h>
#include <string.h>

static char *flag = "{strings are bytes, too}You'll never make me talk!";

int main(int argc, char *argv[]) {
    puts(strstr(flag, "}") + 1);
}
