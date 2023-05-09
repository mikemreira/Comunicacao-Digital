// Exercise 4 from the first practical class in c language

#include <stdio.h>
#include <stdlib.h>

#define MASK 0x01
#define ASCII_LEN 128
#define NOT_MASK 0x7F

//4.a

int count_ones(int val){
    int count = 0;
    while(val > 0){
        count += (val & MASK);
        val >>= 1;
    }
    return count;
}

int count_zeros(int val){
    int count = 0;
    while(val > 0){
        count += !(val & MASK);
        val >>= 1;
    }
    return count;
}

//4.b

void print_bits(int val){
    while(val > 0){
        printf("%i", (val & MASK) ? 1 : 0);
        val >>= 1;
    }
    printf("\n");
}

//4.c

char most_frequent_symbol(char* file_name){
    int characters[ASCII_LEN];
    int max;
    FILE* fptr = fopen(file_name, "r");
    if(fptr == NULL){
        printf("No such file\n");
        exit(-1);
    }
    for(int i = 0; i < ASCII_LEN; i++){
        characters[i] = 0;
    }
    while(1){
        char c = fgetc(fptr);
        if(c == EOF) break;
        characters[(int) c]++;
    }
    fclose(fptr);
    max = characters[0];
    char most_frequent = (char) 0;
    for(int i = 1; i < ASCII_LEN; i++){
        if(characters[i] > max){
            max = characters[i];
            most_frequent = (char) i;
        }
    }
    printf("Most frequent symbol is %c and it appears %d times\n", most_frequent, max);
    return most_frequent;
}

//4.d

void negative_file(char* input_file_name, char* output_file_name){
    FILE* f1_ptr = fopen(input_file_name, "r");
    FILE* f2_ptr = fopen(output_file_name, "w");
    if(f1_ptr == NULL){
        printf("No such input file\n", stderr);
        exit(-1);
    }
    while(1){
        char c = fgetc(f1_ptr);
        if(c == EOF) break;
        unsigned char negated = (~ (int) c) & NOT_MASK;
        fprintf(f2_ptr, "%c", negated);
    }
    fclose(f1_ptr);
    fclose(f2_ptr);
}

int main(){
    printf("%d\n", count_ones(7));
    printf("%d\n", count_zeros(8));
    print_bits(8);
    printf("%c\n", most_frequent_symbol("me.txt"));
    negative_file("me.txt", "me_out.txt");
}