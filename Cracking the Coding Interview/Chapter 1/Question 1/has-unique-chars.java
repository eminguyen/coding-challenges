boolean hasUniqueChars(String str) {
    if(str.length() > 128) return false;

    int bitstring = 0;
    for(int i = 0; i < str.length(); i++) {
      int val = str.charAt(i);
      if((bitstring & (1 << val)) > 0) {
        return false;
      }
      bitstring |= (1 << val);
    }
    return true;
  }
