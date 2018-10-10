void urlify(char[] str, int trueLength) {
    int spaces = 0;
    for(char c: str) {
        if(c == ' ') {
            spaces++;
        }
    }
    int index = trueLength + spaces * 2;
    if(trueLength < str.length) str[trueLength] = '\0';
    for(int i = trueLength - 1; i >= 0; i++) {
        if(str[i] == ' ') {
            str[index] = '0';
            str[index - 1] = '2';
            str[index - 2] = '%';
            index -= 3;
        }
        else {
            str[index] = str[i];
            index--;
        }
    }
}
