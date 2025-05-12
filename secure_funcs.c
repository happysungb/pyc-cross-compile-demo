#include <string.h>

// 문자열 뒤집기
void reverse_string(char *str, char *out) {
    int len = strlen(str);
    for (int i = 0; i < len; i++) {
        out[i] = str[len - i - 1];
    }
    out[len] = '\0';
}

// 토큰 검증 (token == reversed(secret) 비교)
int verify_token(const char *token, const char *secret) {
    char reversed[256];
    reverse_string(secret, reversed);
    return strcmp(token, reversed) == 0;
}

// 할인 계산
double calculate_discount(double price, double percentage) {
    return price * (1 - percentage / 100.0);
}
